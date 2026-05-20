# quanttide-base 用户文档

## 安装

```bash
pip install quanttide-base
```

## 快速开始

```python
from quanttide_base.storage import get_data_dir, get_config_dir

data_dir = get_data_dir("my-app")
config_dir = get_config_dir("my-app")

# 数据目录
# Linux:   ~/.local/share/quanttide/my-app/
# macOS:   ~/Library/Application Support/quanttide/my-app/
# Windows: %APPDATA%/quanttide/my-app/
```

## API 参考

| 函数 | 说明 |
|------|------|
| `get_config_dir(app_name)` | 应用配置目录 |
| `get_data_dir(app_name)` | 应用数据目录 |
| `get_cache_dir(app_name)` | 应用缓存目录 |
| `get_log_dir(app_name)` | 应用日志目录 |
| `get_state_dir(app_name)` | 应用状态目录 |
| `get_runtime_dir(app_name)` | 应用运行时目录 |

## 环境变量

```
<APP>_CONFIG_HOME
<APP>_DATA_HOME
<APP>_CACHE_HOME
<APP>_LOG_HOME
```

## 相关文档

- [开发指引](/docs/dev/local_storage.md)
- [存储规范](/docs/spec/local_storage.md)
