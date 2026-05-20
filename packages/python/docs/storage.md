# 本地存储

`LocalStorage` 提供跨平台的本地目录管理，遵循各平台规范（Linux XDG、macOS、Windows Known Folders）。

## 用法

```python
from quanttide import LocalStorage

store = LocalStorage("my-app")
```

### 获取目录

```python
store.config_dir   # 配置目录（settings.json 等）
store.data_dir     # 持久数据（数据库、项目文件）
store.state_dir    # 可丢弃状态（历史记录）
store.cache_dir    # 临时数据（网络缓存、缩略图）
store.log_dir      # 运行日志
store.runtime_dir  # 会话级文件（socket、锁）
```

首次访问自动创建目录（权限 `0700`）。

### 平台路径对照

| 类别 | Linux | macOS | Windows |
|------|-------|-------|---------|
| config | `~/.config/quanttide/<app>` | `~/Library/Preferences/quanttide/<app>` | `%APPDATA%\quanttide\<app>` |
| data | `~/.local/share/quanttide/<app>` | `~/Library/Application Support/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>` |
| cache | `~/.cache/quanttide/<app>` | `~/Library/Caches/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>\Cache` |

## 环境变量

每个目录可通过环境变量覆写：

```bash
export MY_APP_DATA_HOME=/custom/path
```

命名规则：`<APP>_<CATEGORY>_HOME`，app 名大写、连字符变下划线。

优先级：**应用级环境变量 > 平台默认路径**

## 运行时目录回退

Linux 上 `XDG_RUNTIME_DIR` 可能未设置，此时自动回退到 `cache/run` 并发出告警：

```python
>>> store.runtime_dir
UserWarning: RUNTIME_DIR not available, fallback to /home/user/.cache/quanttide/my-app/run
```

## API

| 属性 | 类型 | 说明 |
|------|------|------|
| `config_dir` | `Path` | 配置目录 |
| `data_dir` | `Path` | 数据目录 |
| `state_dir` | `Path` | 状态目录 |
| `cache_dir` | `Path` | 缓存目录 |
| `log_dir` | `Path` | 日志目录 |
| `runtime_dir` | `Path` | 运行时目录 |

## 相关规范

- [存储规范](/docs/spec/local_storage.md)
