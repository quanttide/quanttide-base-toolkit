"""量潮标准字段。

提供跨语言一致的字段类型，可在 Pydantic 模型中直接用作类型注解。

用法:
    >>> from pydantic import BaseModel
    >>> from quanttide import IdField, NameField, TitleField

    >>> class Project(BaseModel):
    ...     id: IdField
    ...     name: NameField
    ...     title: TitleField | None = None

    >>> p = Project(id="00000000-0000-0000-0000-000000000001", name="my-project")
    >>> p.title is None
    True
"""

from .audit import CreatedAtField, UpdatedAtField
from .identifier import IdField, LabelField, NameField, OrderField
from .text import DescriptionField, TitleField

__all__ = [
    "IdField",
    "NameField",
    "OrderField",
    "LabelField",
    "TitleField",
    "DescriptionField",
    "CreatedAtField",
    "UpdatedAtField",
]
