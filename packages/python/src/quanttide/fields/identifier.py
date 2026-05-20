from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class IdField:
    """全局唯一主键"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.uuid_schema()


class OrderField:
    """排序序号，自增"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.int_schema()


class NameField:
    """短字符串标识（≤100），slug 风格"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=100)


class LabelField:
    """短字符串（≤50），枚举值的人眼可读展示"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=50)
