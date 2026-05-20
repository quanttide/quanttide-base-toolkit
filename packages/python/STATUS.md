# quanttide Python SDK — 状态报告

## 当前范围

- `storage` 模块（`LocalStorage` 类）— ✅ 已完成
- `fields` 模块（标准字段 Pydantic 类型）— ✅ v0.1.1 已完成

## 验收结果

| 检查项 | 结果 |
|:------|:----|
| API 可用 | ✅ 8 个字段 + 6 个存储属性全部实现 |
| 环境变量覆写 | ✅ 6 个类别均支持 |
| 编译构建 | ✅ `hatchling build` 通过 |
| 类型标记 | ✅ `py.typed` 已放置 |
| 测试总数 | ✅ 29 个，全部通过，含 doctest |
| 覆盖率 | ✅ 100% |

## 已知问题

| # | 问题 | 文件 | 状态 |
|---|------|------|------|
| 5 | `fields/` 仅提供 Pydantic 类型，无 SQLAlchemy `TypeDecorator` 映射 | `src/quanttide/fields/` | 🟡 待规划 |
| 6 | `TypeField` / `CategoryField` / `StatusField` 是基类（需继承），其他字段是类型（直接注解），用法分裂 | `src/quanttide/fields/` | 🟡 待规划 |
| 7 | `ContentField` spec 声明"多模态"但实现为纯字符串 | `src/quanttide/fields/text.py` | 🟡 待规划 |
