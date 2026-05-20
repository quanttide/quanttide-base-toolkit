# quanttide Python SDK

量潮基础工具箱的 Python SDK，提供跨平台的本地存储等基础能力。

## 设计原则

- **平台自适应**：遵循各平台事实标准（XDG、Windows Known Folders、macOS File System Programming Guide）
- **零外部依赖（核心层）**：仅依赖 `platformdirs` 和标准库
- **命名空间隔离**：路径统一为 `<平台基础目录>/quanttide/<应用名>/`

## 安装

```bash
pip install quanttide
```

## 快速开始

```python
from quanttide import LocalStorage

store = LocalStorage("my-app")
data_dir = store.data_dir
config_dir = store.config_dir

# 数据目录
# Linux:   ~/.local/share/quanttide/my-app/
# macOS:   ~/Library/Application Support/quanttide/my-app/
# Windows: %APPDATA%/quanttide/my-app/
```

## API 参考

### 本地存储

| 属性 | 说明 |
|------|------|
| `store.config_dir` | 应用配置目录 |
| `store.data_dir` | 应用数据目录 |
| `store.cache_dir` | 应用缓存目录 |
| `store.log_dir` | 应用日志目录 |
| `store.state_dir` | 应用状态目录 |
| `store.runtime_dir` | 应用运行时目录 |

### 标准字段

```python
from quanttide import IdField, NameField, TitleField
from pydantic import BaseModel

class Project(BaseModel):
    id: IdField
    name: NameField
    title: TitleField | None = None
```

| 字段类 | 值类型 | 说明 |
|--------|--------|------|
| `IdField` | UUID | 全局唯一主键 |
| `NameField` | str（≤100） | 唯一标识名，slug 风格 |
| `OrderField` | int（≥1） | 排序序号 |
| `LabelField` | str（≤50） | 显示标签 |
| `TitleField` | str（≤255） | 完整标题 |
| `DescriptionField` | str | 描述 |
| `CreatedAtField` | datetime | 创建时间 |
| `UpdatedAtField` | datetime | 最后更新时间 |

字段规范见 [标准字段规范](/docs/spec/standard_fields.md)。

## 环境变量

```text
<APP>_CONFIG_HOME
<APP>_DATA_HOME
<APP>_STATE_HOME
<APP>_CACHE_HOME
<APP>_LOG_HOME
<APP>_RUNTIME_HOME
```

## 开发

```bash
uv sync --dev

# lint
uv run ruff check src/ tests/

# test (includes doctests)
uv run pytest --cov=src/
```

## 相关文档

- [存储规范](/docs/spec/local_storage.md)
- [本地存储开发指引](/docs/dev/local_storage.md)
