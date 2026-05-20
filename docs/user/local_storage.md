# 本地存储

## 安装

```bash
pip install quanttide-base-toolkit
```

## 快速开始

```python
from quanttide_base_toolkit.storage import get_data_dir

data_dir = get_data_dir("my-app")
# Linux:   ~/.local/share/quanttide/my-app/
# macOS:   ~/Library/Application Support/quanttide/my-app/
# Windows: %LOCALAPPDATA%\quanttide\my-app\
```

## 可用函数

| 函数 | 返回 | 用途 |
|------|------|------|
| `get_config_dir(appname)` | `Path` | 配置文件（`settings.json` 等） |
| `get_data_dir(appname)` | `Path` | 持久化数据（数据库、项目文件） |
| `get_state_dir(appname)` | `Path` | 可丢弃的状态（历史记录、缓存索引） |
| `get_cache_dir(appname)` | `Path` | 可删除的临时数据（网络缓存、缩略图） |
| `get_log_dir(appname)` | `Path` | 运行日志 |
| `get_runtime_dir(appname)` | `Path` | 会话级文件（socket、锁） |

所有函数在首次调用时自动创建目录（权限 `0700`）。

## 环境变量

每个目录可通过环境变量强制指定路径：

```bash
export MYAPP_DATA_HOME=/custom/path
```

命名规则：`<APPNAME>_<CATEGORY>_HOME`，`APPNAME` 转为大写、连字符变下划线。

## 示例

```python
from quanttide_base_toolkit.storage import get_config_dir, get_data_dir, get_cache_dir

config = get_config_dir("qtcloud-knowl") / "settings.json"
data   = get_data_dir("qtcloud-knowl")
cache  = get_cache_dir("qtcloud-knowl")

# config.read_json() / data.mkdir() / cache.iterdir() ...
```

## 相关文档

- [实现细则](../dev/local_storage.md) — 接口设计、平台差异、测试策略
- [存储规范](../spec/local_storage.md) — 公司目录规范、备份策略、路径对照表
