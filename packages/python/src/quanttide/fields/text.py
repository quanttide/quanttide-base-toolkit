from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class TitleField:
    """完整标题（≤255）。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import TitleField
        >>> class M(BaseModel):
        ...     title: TitleField
        >>> m = M(title="My Project")
        >>> m.title
        'My Project'
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=255)


class DescriptionField:
    """描述（长文本）。

    用法:
        >>> from pydantic import BaseModel
        >>> from quanttide import DescriptionField
        >>> class M(BaseModel):
        ...     desc: DescriptionField
        >>> m = M(desc="some long text")
        >>> m.desc
        'some long text'
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema()
