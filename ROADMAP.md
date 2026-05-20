# ROADMAP

> 背景：`quanttide-base-toolkit`（`flutter-quanttide` + `django-quanttide`）为 2-3 年前早期设计。当前进入 AI 原生时代，开发范式正在转变，本路线图重新审视工具包定位与演进方向。

---

## 现状盘点

| 包 | 版本 | 阶段 | 核心能力 |
|---|------|------|---------|
| `flutter_quanttide` | v0.2.0-alpha.2 | 早期原型 | ApiClient、BLoC 骨架、网络组件、recase 工具 |
| `django-quanttide` | v0.1.0-beta.6 | 早期原型 | 基础 Django 扩展（多态模型等） |
| `docs/` | — | 规格草稿 | localStorage 规范，但未在任何包中实现 |

**共同问题**：
- 两三年未实质迭代，技术选型停留在上一个时代
- 文档与实现脱节
- 缺少统一的跨平台设计理念

---

## AI 原生时代的影响

AI 原生开发（Cursor、Copilot、AI Agent 等）对基础工具包提出新要求：

1. **AI 生成友好** — 清晰的类型定义和一致的代码模式，便于 AI 理解和生成
2. **声明式 > 命令式** — schema/配置驱动比手写胶水代码更适合 AI 理解和生成
3. **文档即代码** — 类型注解和文档字符串比单独的外置文档更有价值（AI 训练数据来源）
4. **跨平台统一** — AI 开发不考虑平台边界，工具包应提供一致的抽象层
5. **工具包不做 Agent** — MCP 协议封装、Agent 集成等在 `quanttide-agent` 中实现，toolkit 保持纯基础设施定位

---

## 版本目标

### Python SDK v0.1.1

- [ ] **标准字段模型**：将 django-quanttide 定义的 14 个标准字段（IDField、NameField、TitleField、DescriptionField、TypeField、StatusField 等）移植为 Python SDK 的 Pydantic 类型，使非 Django 项目（FastAPI、普通 Python 服务等）也能复用同一套字段语义
- [ ] **跨语言字段对照**：对齐 Python（Pydantic）与 Dart（freezed）的标准字段定义，使前后端共享同一套数据契约

## 路线图

### 阶段一：清理与评估（当前）

- [ ] 确定 monorepo 定位：base-toolkit 是继续维护还是归档？
- [ ] 评估两个包的活跃用户 / 依赖方
- [ ] 清理过期文档（docs/、TODO.md、CHANGELOG.md）
- [ ] 决定 flutter-quanttide 是否继续发展

### 阶段二：重塑定位（如果继续）

- [ ] 重新定义 `quanttide-base-toolkit` 为 **AI-native application toolkit**
- [ ] 深化 BLoC 模式：完善事件/状态定义、补齐 Bloc/Cubit 实现，形成完整的状态管理最佳实践
- [ ] 引入 schema-first 设计：OpenAPI / JSON Schema 驱动 API 客户端生成
- [ ] 跨平台统一：确保 Dart 和 Python 包共享相同的数据模型语义

### 阶段三：AI 生成优化

- [ ] API Client 支持 OpenAPI 描述文件直接生成类型安全的调用接口
- [ ] 提供标准化代码模板与模式库，优化 AI 代码生成质量
- [ ] 类型系统强化：充分利用 Dart 和 Python 的类型注解，作为 AI 理解的"契约"
- [ ] 本地存储等基础设施对接 AI Agent 的 sandbox 需求（接口由 `quanttide-agent` 消费）

### 阶段四：生态建设

- [ ] 发布稳定版 v1.0.0（flutter / django 同步）
- [ ] 提供 `quanttide-base-toolkit` CLI 工具（脚手架、代码生成）
- [ ] 完善测试与文档，使之成为 AI 训练语料级质量的代码库

---

## 关键决策点

1. **继续还是归档？** — 如果无活跃用户，建议归档冻结，新项目按新思路另起炉灶。BLoC 模式保留并深化。
2. **跨语言统一到什么程度？** — Flutter（前端）和 Django（后端）在 AI 时代是分别演进还是保持同一套声明式描述
3. **与 quanttide-agent 的边界** — toolkit 提供基础设施接口，Agent 集成（MCP 等）在 `quanttide-agent` 实现
