# quanttide

量潮基础工具箱的 Python SDK。

## 安装

```bash
pip install quanttide
```

## 快速开始

```python
from quanttide import LocalStorage

store = LocalStorage("my-app")
data_dir = store.data_dir

# Linux:   ~/.local/share/quanttide/my-app/
# macOS:   ~/Library/Application Support/quanttide/my-app/
# Windows: %APPDATA%/quanttide/my-app/
```

标准字段与 Pydantic 模型搭配使用：

```python
from pydantic import BaseModel
from quanttide import IdField, NameField, TitleField

class Project(BaseModel):
    id: IdField
    name: NameField
    title: TitleField | None = None
```

## API

### LocalStorage

| 属性 | 返回值 | 说明 |
|------|--------|------|
| `config_dir` | `Path` | 配置目录 |
| `data_dir` | `Path` | 数据目录 |
| `state_dir` | `Path` | 状态目录 |
| `cache_dir` | `Path` | 缓存目录 |
| `log_dir` | `Path` | 日志目录 |
| `runtime_dir` | `Path` | 运行时目录 |

### 标准字段

| 字段类 | Python 类型 | 说明 |
|--------|-------------|------|
| `IdField` | `UUID` | 全局唯一主键 |
| `NameField` | `str`（≤100） | 唯一标识名 |
| `OrderField` | `int`（≥1） | 排序序号 |
| `LabelField` | `str`（≤50） | 显示标签 |
| `TitleField` | `str`（≤255） | 完整标题 |
| `DescriptionField` | `str` | 描述 |
| `CreatedAtField` | `datetime` | 创建时间 |
| `UpdatedAtField` | `datetime` | 最后更新时间 |

## 开发

```bash
uv sync --dev
uv run pytest --cov=src/   # 含 doctest
uv run ruff check src/ tests/
```

## 相关文档

- [标准字段](/docs/spec/standard_fields.md) — 跨语言规范
- [存储使用手册](docs/storage.md) — LocalStorage 用法
- [字段使用手册](docs/fields.md) — 标准字段用法
- [存储规范](/docs/spec/local_storage.md)
