# 开发者文档

## 目录结构

```
src/quanttide/
  __init__.py       # 公开 API（storage + fields）
  storage.py        # LocalStorage 实现
  fields/
    __init__.py     # 模块入口，含用法 doctest
    identifier.py   # IdField, NameField, OrderField, LabelField
    text.py         # TitleField, DescriptionField
    audit.py        # CreatedAtField, UpdatedAtField
tests/
  test_storage.py   # storage 模块测试（14 个）
  test_fields.py    # fields 模块测试（15 个）
docs/
  README.md         # 本文件
```

## 约定

- **类型注解优先**：所有字段类在 Pydantic 模型中直接用作类型注解，`| None` 表示可选
- **doctest 即文档**：所有公开 API 的 docstring 包含可执行的用法示例
- **跨语言一致**：字段定义与 Dart 端共享同一份 spec（`docs/spec/standard_fields.md`）

## 本地开发

```bash
uv sync --dev
uv run pytest --cov=src/
uv run ruff check src/ tests/
```

## 构建

```bash
uv build
```

## 字段类实现模式

每个字段类是一个 Pydantic 自定义类型，通过 `__get_pydantic_core_schema__` 定义校验规则：

```python
class NameField:
    """唯一标识名（≤100），slug 风格"""
    @classmethod
    def __get_pydantic_core_schema__(cls, _source, _handler):
        return core_schema.str_schema(max_length=100)
```

枚举字段（TypeField、StatusField 等）待确认后通过继承 `StrEnum` 实现。
