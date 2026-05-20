# 应用数据目录规范

> 遵循各平台事实标准：Linux XDG Base Directory、Windows Known Folders、macOS File System Programming Guide。
>
> 实现指引见 [dev/local_storage.md](../dev/local_storage.md)。

## 1. 目标与范围

**目标**：统一公司所有 CLI 工具和桌面应用在用户设备上的文件存放位置，便于统一备份、安全审计、故障排查和设备迁移。

**适用范围**：所有面向用户设备运行的应用（Linux、macOS、Windows）。纯服务端容器化部署不在此列。

**核心原则**：遵守各平台事实标准，不自行发明目录结构；通过统一抽象层屏蔽平台差异。

## 2. 目录分类

| 类别 | 内容举例 | 可删除 | 备份 | Windows 漫游 |
|------|---------|--------|------|-------------|
| 配置 | 偏好设置、密钥文件 | 否 | 定期 | Roaming |
| 数据 | 项目文件、数据库、插件 | 否 | 按需 | Local |
| 状态 | 历史记录、最近文件列表 | 丢失不影响核心功能 | 可选 | Local |
| 缓存 | 网络缓存、预编译对象 | 随时可删 | 不备份 | Local |
| 运行时 | IPC socket、锁文件 | 会话结束后 | 不备份 | Local |
| 日志 | 运行日志 | 建议保留 30 天 | 通常不备份 | Local |

## 3. 命名空间

所有应用路径遵循同一结构：

```
<平台基础目录>/quanttide/<应用名>/
```

- **组织标识**：固定为 `quanttide`
- **应用标识**：小写，连字符分隔（如 `qtcloud-knowl`、`qtcloud-write`）

## 4. 平台路径对照

| 类别 | Linux | macOS | Windows |
|------|-------|-------|---------|
| 配置 | `~/.config/quanttide/<app>` | `~/Library/Preferences/quanttide/<app>` | `%APPDATA%\quanttide\<app>` |
| 数据 | `~/.local/share/quanttide/<app>` | `~/Library/Application Support/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>` |
| 状态 | `~/.local/state/quanttide/<app>` | `~/Library/Application Support/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>` |
| 缓存 | `~/.cache/quanttide/<app>` | `~/Library/Caches/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>\Cache` |
| 日志 | `~/.local/state/quanttide/<app>/log` | `~/Library/Logs/quanttide/<app>` | `%LOCALAPPDATA%\quanttide\<app>\log` |
| 运行时 | `$XDG_RUNTIME_DIR/quanttide/<app>` | `~/Library/Caches/TemporaryItems/quanttide/<app>` | `%TEMP%\quanttide\<app>` |

**平台差异说明**：

- **Windows**：配置目录使用 `APPDATA`（Roaming），保证企业域环境下配置随用户漫游；其余类别使用 `LOCALAPPDATA`。
- **macOS**：状态和数据共用 `Application Support`，应用内部以 `data/`、`state/` 子目录区分。
- **Linux**：`XDG_RUNTIME_DIR` 可能不存在，应用必须回退到 `~/.cache/quanttide/<app>/run` 并给出告警。

## 5. 环境变量

每个目录可通过独立环境变量覆盖。命名规则：`<应用名>_<类别>_HOME`，应用名转为大写，连字符变下划线。

优先级：**应用级环境变量 > 平台原生环境变量 > 规范默认值**

禁止在代码中硬编码路径，必须通过 `platformdirs` 等专用库获取。

## 6. 备份与清理

- 配置目录应纳入定期备份
- 缓存目录可被系统清理工具安全删除
- 日志目录应设置轮转策略，保留 30 天
- 应用不得因缓存或日志缺失而拒绝启动
