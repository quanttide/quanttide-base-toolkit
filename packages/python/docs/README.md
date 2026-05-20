# quanttide-base Python SDK

## 定位

`quanttide-base` 是量潮基础工具箱的 Python SDK，提供跨平台的本地存储、配置管理、文件路径等基础能力。

## 设计原则

- **平台自适应**：遵循各平台事实标准（XDG、Windows Known Folders、macOS File System Programming Guide）
- **零外部依赖**（核心层）：仅依赖 `platformdirs` 和标准库
- **不可变数据模型**：所有领域对象使用 Pydantic `BaseModel(frozen=True)`
- **命名空间隔离**：路径统一为 `<平台基础目录>/quanttide/<应用名>/`

## 模块划分

| 模块 | 职责 | 状态 |
|------|------|------|
| `quanttide_base.storage` | 本地目录管理（配置/数据/缓存/日志等） | 计划中 |
| `quanttide_base.models` | 跨应用共享的 Pydantic 领域模型 | 计划中 |

## 安装

```bash
pip install quanttide-base
```

## 开发

```bash
cd packages/python
uv sync --dev

# lint
uv run ruff check src/ tests/

# test
uv run pytest --cov=src/
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

- [存储规范](/docs/spec/local_storage.md)
- [本地存储开发指引](/docs/dev/local_storage.md)
