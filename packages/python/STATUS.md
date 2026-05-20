# quanttide Python SDK — 状态报告

## 当前范围

- `storage` 模块（`LocalStorage` 类）— ✅ 已完成
- `fields` 模块（标准字段 Pydantic 类型）— ✅ v0.1.1 已完成

## 验收结果

| 检查项 | 结果 |
|:------|:----|
| API 可用 | ✅ 6 个属性全部实现 |
| 环境变量覆写 | ✅ 6 个类别均支持 |
| 编译构建 | ✅ `hatchling build` 通过 |
| 类型标记 | ✅ `py.typed` 已放置 |
| 测试总数 | ✅ 14 个，全部通过 |
| 覆盖率 | ✅ 100%（含异常分支） |

## 已知问题

| # | 问题 | 文件 | 影响 | 状态 |
|---|------|------|------|------|
| 1 | `pyproject.toml` 的 `readme` 指向空 `README.md`，实际文档在 `docs/README.md` | `pyproject.toml:5` | PyPI 展示为空 | ✅ 已修复 |
| 2 | 测试未覆盖 `PermissionError` 和 `OSError` 异常分支 | `tests/test_storage.py` | 回归防护弱 | ✅ 已修复 |
| 3 | 环境变量测试用 `del os.environ` 清理 | `tests/test_storage.py` | 测试隔离性弱 | ✅ 已修复（改用 `monkeypatch`） |
| 4 | `pyproject.toml` 缺少 `[project.urls]` 和 `keywords` 等 PyPI 元信息 | `pyproject.toml` | PyPI 展示不完整 | ✅ 已修复 |
| 5 | `fields/` 仅提供 Pydantic 类型，无 SQLAlchemy `TypeDecorator` 映射 | `src/quanttide/fields/` | 使用者需在 ORM 层重定义约束 | 🟡 待规划 |
| 6 | `TypeField` / `CategoryField` / `StatusField` 是基类（需继承），其他字段是类型（直接注解），用法分裂 | `src/quanttide/fields/` | 使用者体验不一致 | 🟡 待规划 |
| 7 | `ContentField` spec 声明"多模态"但实现为纯字符串 | `src/quanttide/fields/text.py` | 实现未达 spec 预期 | 🟡 待规划 |

## 文件结构

```
src/quanttide/
  __init__.py       # 导出 LocalStorage + 字段
  storage.py        # LocalStorage 实现
  fields/
    __init__.py     # 导出全部字段
    identifier.py   # IdField, NameField, OrderField, LabelField
    text.py         # TitleField, DescriptionField
    audit.py        # CreatedAtField, UpdatedAtField
  py.typed          # PEP 561 类型标记
tests/
  __init__.py
  test_storage.py   # 14 个测试
pyproject.toml      # 项目配置
README.md           # 使用文档
STATUS.md           # 本文件
TODO.md             # 待办事项
```
