# 标准字段规范

> 跨语言不变的字段定义。

## 标识

| 字段 | 值 | 唯一性 | 用途 |
|------|----|--------|------|
| `id` | UUID | 全局 | 唯一主键 |
| `order` | 整数 | 模型内 | 排序序号，自增 |
| `name` | 短字符串（≤100） | 模型内 | 唯一标识名，slug 风格 |
| `label` | 短字符串（≤50） | 不要求 | 枚举值的人眼可读展示。与 `title` 的区别：`title` 标识记录内容，`label` 标识枚举值展示。与 `name` 的区别：`name` 是唯一机器标识，`label` 是可读别名 |

## 文本

| 字段 | 值 | 用途 |
|------|----|------|
| `title` | 字符串（≤255） | 完整标题 |
| `description` | 长文本 | 描述 |
| `content` | 多模态 | 富文本正文 |

## 分类

| 字段 | 值 | 用途 |
|------|----|------|
| `type` | 枚举 | 系统分类 |
| `category` | 枚举/引用 | 类别，与 type/tag 并列 |
| `tag` | 枚举集合 | 标签，与 type/category 并列 |

`type`、`category`、`tag` 三者并列，描述不同维度的分类。

## 状态

| 字段 | 值 | 用途 |
|------|----|------|
| `status` | 枚举 | 生命周期状态 |

## 审计

| 字段 | 值 | 用途 |
|------|----|------|
| `created_at` | 时间点 | 创建时间，不可变 |
| `updated_at` | 时间点 | 最后更新时间 |
| `created_by` | 用户引用 | 创建者 |
| `updated_by` | 用户引用 | 最后更新者 |

## 版本

| 版本 | 变更 |
|------|------|
| v0.1（django） | `id` `order` `name` `verboseName` `title` `description` `readme` `type` `status` `stage` + 审计 |
| v0.2 | `order` 替代 `number`；`label` 替代 `verboseName`（限定范围）；`content` 替代 `readme`；删除 `stage`；新增 `category`、`tag` |
