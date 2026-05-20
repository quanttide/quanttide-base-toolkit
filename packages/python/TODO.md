# TODO

## v0.1.1

- [x] 标准字段模型：移植为 Pydantic 类型，5 类 15 个字段

## 已完成

- [x] 补充测试覆盖 `PermissionError` 和 `OSError` 异常分支
- [x] 环境变量测试改用 `monkeypatch` fixture，废弃 `del os.environ` 方式
- [x] 补充 `[project.urls]`、`keywords` 等 PyPI 元信息
