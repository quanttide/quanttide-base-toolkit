# 标准字段规范

> 跨语言不变的字段定义。未完全确定的字段标记为 **TBD**。

## 标识

| 字段 | 值 | 唯一性 | 用途 |
|------|----|--------|------|
| `id` | UUID | 全局 | 唯一主键 |
| `order` | 正整数 | 模型内 | 排序序号 |
| `name` | 短字符串（≤100） | 模型内 | 唯一标识名，slug 风格 |
| `label` | 短字符串（≤50） | 不要求 | 显示标签 |

## 文本

| 字段 | 值 | 用途 |
|------|----|------|
| `title` | 字符串（≤255） | 完整标题 |
| `description` | 字符串 | 描述 |
| `content` | **TBD** | 富文本正文 |

## 分类

| 字段 | 值 | 用途 |
|------|----|------|
| `type` | **TBD** | 系统分类 |
| `category` | **TBD** | 类别 |
| `tag` | **TBD** | 标签 |

## 状态

| 字段 | 值 | 用途 |
|------|----|------|
| `status` | **TBD** | 生命周期状态 |

## 审计

| 字段 | 值 | 用途 |
|------|----|------|
| `created_at` | 时间点 | 创建时间，不可变 |
| `updated_at` | 时间点 | 最后更新时间 |
| `created_by` | **TBD** | 创建者 |
| `updated_by` | **TBD** | 最后更新者 |

## 已确认字段（v0.1.1）

```python
# 可用字段类
IdField           # UUID
NameField         # str, ≤100, slug
OrderField        # int, 正整数
LabelField        # str, ≤50
TitleField        # str, ≤255
DescriptionField  # str
CreatedAtField    # datetime
UpdatedAtField    # datetime
```

其余字段待后续版本确认。
