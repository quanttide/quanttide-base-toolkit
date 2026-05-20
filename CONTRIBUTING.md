# 项目约定

## 目录结构

```
quanttide-base-toolkit/
├── packages/     → 各语言/框架的 SDK/工具包
│   └── flutter/  → Flutter SDK (quanttide/flutter-quanttide)
├── docs/         → 文档
│   ├── spec/
│   ├── dev/
│   └── user/
└── CONTRIBUTING.md
```

## 版本发布规范

### Tag 命名

同一仓库内包含多语言包，tag 使用 `{lang}/v{version}` 格式避免冲突：

```
flutter/v0.2.0-alpha.2
dart/v0.1.0
python/v0.1.0
```

| 语言 | prefix |
|------|--------|
| Flutter | `flutter/` |
| Dart | `dart/` |
| Python | `python/` |
| Django | `django/` |

### 发布流程

1. 更新对应语言包的版本号（`pubspec.yaml`、`pyproject.toml` 等）
2. 创建 tag：`git tag {lang}/v{版本}`
3. 推送 tag：`git push origin {lang}/v{版本}`
4. 创建 GitHub Release，关联该 tag
