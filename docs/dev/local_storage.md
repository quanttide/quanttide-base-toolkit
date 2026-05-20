# 本地存储 — 开发指引

> 基于 [spec/local_storage.md](../spec/local_storage.md) 的实现细则。

## 核心抽象

所有平台路径差异由 `platformdirs`（Python）或等价库屏蔽，业务代码**禁止**直接拼接路径。

```python
# ❌ 禁止
Path.home() / ".local" / "share" / "quanttide" / APPNAME

# ✅ 正确
user_data_dir(APPNAME, VENDOR)
```

## 目录服务接口

每个应用通过统一封装获取六个目录：

| 函数 | 返回 | 自动创建？ | 权限 |
|------|------|-----------|------|
| `get_config_dir()` | `Path` | 是（0700） | 读写 |
| `get_data_dir()` | `Path` | 是（0700） | 读写 |
| `get_state_dir()` | `Path` | 是（0700） | 读写 |
| `get_cache_dir()` | `Path` | 是（0700） | 读写 |
| `get_log_dir()` | `Path` | 是（0700） | 只写 |
| `get_runtime_dir()` | `Path` | 是（0700） | 读写 |

## 环境变量覆写

每个目录支持独立的环境变量覆盖，命名规则：`<APP>_<CATEGORY>_HOME`。

优先级：**应用级环境变量 > 平台原生环境变量 > 默认值**

```python
def _from_env_or_default(category: str, default_fn) -> Path:
    env_var = f"{APPNAME.upper().replace('-', '')}_{category}_HOME"
    override = os.environ.get(env_var)
    return Path(override) if override else default_fn()
```

## 参考实现

```python
# quanttide_base_toolkit/storage.py

from platformdirs import (
    user_config_dir, user_data_dir, user_cache_dir,
    user_state_dir, user_log_dir, user_runtime_dir,
)
from pathlib import Path
import os
import sys

VENDOR = "quanttide"
APPNAME = "my-tool"  # 由各应用传入

def _make_dir(path: str, mode: int = 0o700) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    try:
        p.chmod(mode)
    except PermissionError:
        pass  # 目录已存在且权限正确时忽略
    return p

def get_config_dir(appname: str = APPNAME) -> Path:
    return _make_dir(user_config_dir(appname, VENDOR, roaming=True))

def get_data_dir(appname: str = APPNAME) -> Path:
    return _make_dir(user_data_dir(appname, VENDOR))

def get_cache_dir(appname: str = APPNAME) -> Path:
    return _make_dir(user_cache_dir(appname, VENDOR))

def get_state_dir(appname: str = APPNAME) -> Path:
    return _make_dir(user_state_dir(appname, VENDOR))

def get_log_dir(appname: str = APPNAME) -> Path:
    if sys.platform == "darwin":
        return _make_dir(Path.home() / "Library/Logs" / VENDOR / appname)
    return _make_dir(get_state_dir(appname) / "log")

def get_runtime_dir(appname: str = APPNAME) -> Path:
    try:
        return _make_dir(user_runtime_dir(appname, VENDOR))
    except OSError:
        fallback = get_cache_dir(appname) / "run"
        import warnings
        warnings.warn(f"RUNTIME_DIR not available, fallback to {fallback}")
        return _make_dir(fallback)
```

## 平台差异

| 行为 | Linux | macOS | Windows |
|------|-------|-------|---------|
| 配置漫游 | 不支持 | 不支持 | 支持（依 Roaming） |
| 运行时目录 | `$XDG_RUNTIME_DIR` | `TemporaryItems` | `%TEMP%` |
| 日志专用目录 | 无，归入 state/log | `~/Library/Logs/` | 无，归入 data/log |

## 测试策略

- 单元测试使用 `tmp_path` 模拟目录创建，不依赖真实平台路径
- 环境变量覆写测试：设 `*_HOME` → 验证返回覆盖路径 → 取消设置
- 不测试 `mkdir` 权限（由 `platformdirs` 保障），但测试创建失败的回退路径
