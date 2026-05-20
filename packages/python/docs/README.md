# 开发者文档

## 目录结构

```
src/quanttide/
  __init__.py       # 公开 API（storage + fields）
  storage.py        # LocalStorage 实现
  fields/
    __init__.py
    identifier.py   # IdField, NameField, OrderField, LabelField
    text.py         # TitleField, DescriptionField
    audit.py        # CreatedAtField, UpdatedAtField
tests/
  test_storage.py   # storage 模块测试
  test_fields.py    # fields 模块测试
```

## 本地开发

```bash
uv sync --dev
uv run pytest --doctest-modules --cov=src/
uv run ruff check src/ tests/
```

## 构建

```bash
uv build
```
