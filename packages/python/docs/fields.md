# 标准字段

标准字段是跨语言一致的 Pydantic 自定义类型，直接在模型中用作类型注解。

## 用法

```python
from pydantic import BaseModel
from quanttide import IdField, NameField, TitleField

class Project(BaseModel):
    id: IdField
    name: NameField
    title: TitleField | None = None

p = Project(id="00000000-0000-0000-0000-000000000001", name="my-project")
```

## 字段列表

| 字段类 | Python 类型 | 约束 | 说明 |
|--------|-------------|------|------|
| `IdField` | `UUID` | — | 全局唯一主键 |
| `NameField` | `str` | ≤100 | 唯一标识名，slug 风格 |
| `OrderField` | `int` | ≥1 | 排序序号 |
| `LabelField` | `str` | ≤50 | 显示标签 |
| `TitleField` | `str` | ≤255 | 完整标题 |
| `DescriptionField` | `str` | — | 描述 |
| `CreatedAtField` | `datetime` | — | 创建时间 |
| `UpdatedAtField` | `datetime` | — | 最后更新时间 |

### 可选字段

字段均为可选时用 `| None`：

```python
class Project(BaseModel):
    name: NameField
    title: TitleField | None = None
    description: DescriptionField | None = None
```

### 枚举字段（待确认）

`ContentField`、`TypeField`、`CategoryField`、`TagField`、`StatusField`、`CreatedByField`、`UpdatedByField` 待后续版本确认。

枚举类字段（如 `TypeField`、`StatusField`）将继承 `StrEnum`，由业务模型定义具体枚举值：

```python
from quanttide import TypeField

class ProjectType(TypeField):
    INTERNAL = "internal"
    EXTERNAL = "external"
```

## 校验规则

字段类在创建模型时自动校验：

```python
from pydantic import ValidationError

try:
    Project(name="a" * 101)  # 超过 100 字符
except ValidationError as e:
    print(e.errors()[0]["type"])  # string_too_long
```

## 与 FastAPI 搭配

字段类可直接用于 FastAPI 请求/响应模型：

```python
from fastapi import FastAPI
from pydantic import BaseModel
from quanttide import IdField, NameField

app = FastAPI()

class CreateProjectRequest(BaseModel):
    name: NameField

@app.post("/projects")
def create(req: CreateProjectRequest):
    return {"name": req.name}
```

## 相关规范

- [标准字段规范](/docs/spec/standard_fields.md)
