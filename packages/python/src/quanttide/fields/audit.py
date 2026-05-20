from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class CreatedAtField:
    """创建时间，不可变"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.datetime_schema()


class UpdatedAtField:
    """最后更新时间"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.datetime_schema()
