from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class CreatedAtField:
    """创建时间，不可变。

    用法:
        >>> from datetime import datetime
        >>> from pydantic import BaseModel
        >>> from quanttide import CreatedAtField
        >>> class M(BaseModel):
        ...     created_at: CreatedAtField
        >>> m = M(created_at=datetime(2026, 5, 20))
        >>> m.created_at
        datetime.datetime(2026, 5, 20, 0, 0)
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.datetime_schema()


class UpdatedAtField:
    """最后更新时间。

    用法:
        >>> from datetime import datetime
        >>> from pydantic import BaseModel
        >>> from quanttide import UpdatedAtField
        >>> class M(BaseModel):
        ...     updated_at: UpdatedAtField
        >>> m = M(updated_at=datetime(2026, 5, 20))
        >>> m.updated_at
        datetime.datetime(2026, 5, 20, 0, 0)
    """

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.datetime_schema()
