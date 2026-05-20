# 变更记录

## [0.1.1] - 2026-05-20

### 新增

- 标准字段模块 `fields/`：IdField, NameField, OrderField, LabelField, TitleField, DescriptionField, CreatedAtField, UpdatedAtField
- 测试覆盖 29 个，100%

### 基础设施

- 补充 PyPI 元信息（urls、keywords、classifiers）
- 修复 README 路径
- 启用 doctest 和 coverage 配置

## [0.1.0] - 2026-05-20

### 初始版本

- `LocalStorage` 类，6 个属性：config/data/state/cache/log/runtime
- 支持环境变量 `<APP>_<CATEGORY>_HOME` 覆写
- 运行时目录回退（`XDG_RUNTIME_DIR` 不可用时退到 cache/run）
- 自动目录创建（权限 0700）
- 标准字段：IdField, NameField, OrderField, LabelField, TitleField, DescriptionField, CreatedAtField, UpdatedAtField
- doctest 嵌入源码文档
- 测试覆盖 100%
