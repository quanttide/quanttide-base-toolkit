from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class IdField:
    """全局唯一主键。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import IdField
        >>> class M(BaseModel):
        ...     id: IdField
        >>> m = M(id="00000000-0000-0000-0000-000000000001")
        >>> str(m.id) == "00000000-0000-0000-0000-000000000001"
        True
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.uuid_schema()


class NameField:
    """唯一标识名（≤100），slug 风格。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import NameField
        >>> class M(BaseModel):
        ...     name: NameField
        >>> m = M(name="my-project")
        >>> m.name
        'my-project'
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=100)


class OrderField:
    """排序序号，正整数。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import OrderField
        >>> class M(BaseModel):
        ...     order: OrderField
        >>> m = M(order=1)
        >>> m.order
        1
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.int_schema(ge=1)


class LabelField:
    """显示标签（≤50）。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import LabelField
        >>> class M(BaseModel):
        ...     label: LabelField
        >>> m = M(label="Active")
        >>> m.label
        'Active'
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=50)
