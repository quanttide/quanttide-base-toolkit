# 文档评审状态

评审日期：2026-05-20

## 文档结构

```
docs/
├── spec/local_storage.md    ✅ 规范文档 —— 质量良好
├── user/local_storage.md    ⚠️ 用户文档 —— 内容与实际代码脱节
└── dev/local_storage.md     ⚠️ 开发文档 —— 内容与实际代码脱节
```

## 评审结果

### 🔴 严重问题

| # | 问题 | 涉及文件 | 说明 |
|---|------|---------|------|
| 1 | 文档与实际代码严重脱节 | `user/`, `dev/` | 文档展示 Python 代码（`pip install`、`platformdirs`），但仓库是 Flutter/Dart 项目，且 storage 模块尚未实现 |

### 🟡 中等问题

| # | 问题 | 涉及文件 | 说明 |
|---|------|---------|------|
| 2 | env_var 命名 bug | `dev/local_storage.md:37` | `.replace('-', '')` 删除了连字符，应改为 `.replace('-', '_')` 以符合规范 |
| 3 | state 描述不一致 | `user/local_storage.md` vs `spec/` | user 文档写 "缓存索引"，与 cache 职责重叠 |
| 4 | 跨文档链接不完整 | `spec/` 缺 user 链接 | 三份文档应互相引用形成闭环 |

### 🟢 轻微问题

| # | 问题 | 涉及文件 | 说明 |
|---|------|---------|------|
| 5 | CHANGELOG 过于简陋 | `CHANGELOG.md` | v0.2.0 无日期、无变更条目 |
| 6 | TODO 引用过时模块 | `TODO.md` | `quanttide_design` / `quanttide_testing` 已不存在 |

## 待办事项

- [ ] 实现 Dart/Flutter 的 storage 模块
- [ ] 同步更新三份文档与实际代码一致
- [ ] 修复 `dev/local_storage.md` 中 env_var 的命名 bug
- [ ] 统一 `user/` 与 `spec/` 中 state 的描述
- [ ] 补充跨文档链接
- [ ] 更新 CHANGELOG 和 TODO
