# TODO

## 🔴 高优先级

- [ ] 修复 `pyproject.toml` readme 路径：改为 `docs/README.md`（当前指向空 `README.md`，PyPI 展示为空）

## 🟡 中优先级

- [ ] 补充测试覆盖 `PermissionError` 和 `OSError` 异常分支
- [ ] 环境变量测试改用 `monkeypatch` fixture，废弃 `del os.environ` 方式

## 🟢 低优先级

- [ ] 补充 `[project.urls]`、`keywords` 等 PyPI 元信息

## 待规划

- [ ] `models` 模块开发
