from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class IdField:
    """全局唯一主键"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.uuid_schema()


class NameField:
    """唯一标识名（≤100），slug 风格"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=100)


class OrderField:
    """排序序号，正整数"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.int_schema(ge=1)


class LabelField:
    """显示标签（≤50）"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=50)
