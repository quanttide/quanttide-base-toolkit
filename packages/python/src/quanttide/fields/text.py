from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema


class TitleField:
    """完整标题（≤255）"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema(max_length=255)


class DescriptionField:
    """描述（长文本）"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema()


class ContentField:
    """富文本正文（多模态）"""
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source: type, _handler: GetCoreSchemaHandler
    ) -> CoreSchema:
        return core_schema.str_schema()
