# 开发指引

## 环境准备

```bash
cd packages/python
uv sync --dev
```

## 代码质量

```bash
# lint
uv run ruff check src/ tests/

# test
uv run pytest --cov=src/
```

## 本地存储实现参考

`quanttide_base.storage` 基于 [docs/spec/local_storage.md](/docs/spec/local_storage.md) 实现，核心抽象使用 `platformdirs` 屏蔽平台差异。

### 参考实现

```python
from pathlib import Path
import os
from platformdirs import PlatformDirs

VENDOR = "quanttide"
APPNAME = None  # 由调用方传入

_dirs = PlatformDirs(APPNAME, VENDOR)

def get_data_dir(app_name: str) -> Path:
    """获取应用数据目录"""
    override = os.environ.get(f"{app_name.upper()}_DATA_HOME")
    if override:
        return Path(override)
    return Path(_dirs.user_data_dir) / app_name
```

### 目录分类

参见 [docs/spec/local_storage.md](/docs/spec/local_storage.md) 的 6 种目录分类。
