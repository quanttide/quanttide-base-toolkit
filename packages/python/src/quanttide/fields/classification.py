from enum import StrEnum

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class TypeField(StrEnum):
    """系统分类。继承此类并定义业务枚举值。"""
    pass


class CategoryField(StrEnum):
    """类别。继承此类并定义业务枚举值。"""
    pass


class TagField:
    """标签集合"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.list_schema(core_schema.str_schema())
