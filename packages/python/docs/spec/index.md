# quanttide-base Python SDK 规范

## 定位

`quanttide-base` 是量潮基础工具箱的 Python SDK，提供跨平台的本地存储、配置管理、文件路径等基础能力。

## 设计原则

- **平台自适应**：遵循各平台事实标准（XDG、Windows Known Folders、macOS File System Programming Guide）
- **零外部依赖**（核心层）：仅依赖 `platformdirs` 和标准库
- **不可变数据模型**：所有领域对象使用 Pydantic `BaseModel(frozen=True)`
- **命名空间隔离**：路径统一为 `<平台基础目录>/quanttide/<应用名>/`

## 模块划分

| 模块 | 职责 | 状态 |
|------|------|------|
| `quanttide_base.storage` | 本地目录管理（配置/数据/缓存/日志等） | 计划中 |
| `quanttide_base.models` | 跨应用共享的 Pydantic 领域模型 | 计划中 |
