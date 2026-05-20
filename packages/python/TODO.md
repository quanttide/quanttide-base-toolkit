# TODO

## 已完成

- [x] 标准字段模型：移植为 Pydantic 类型，5 类 15 个字段（v0.1.1）
- [x] 补充测试覆盖 `PermissionError` 和 `OSError` 异常分支
- [x] 环境变量测试改用 `monkeypatch` fixture
- [x] 补充 `[project.urls]`、`keywords` 等 PyPI 元信息
- [x] 修复 `pyproject.toml` readme 路径

## 待规划

- [ ] **#5** 补充 SQLAlchemy `TypeDecorator` 映射，使字段同时覆盖验证层和持久化层
- [ ] **#6** 统一字段用法：全部用 `typing.Annotated` + 元数据，或全部用自定义类型，消除基类 vs 类型注解的分裂
- [ ] **#7** 对齐 `ContentField` 实现与 spec：当前为纯字符串，spec 为"多模态（文本 + 媒体引用）"
