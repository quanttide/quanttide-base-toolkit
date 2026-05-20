from enum import StrEnum


class StatusField(StrEnum):
    """生命周期状态。继承此类并定义业务状态值。

    示例:
        class ProjectStatus(StatusField):
            DRAFT = "draft"
            ACTIVE = "active"
            ARCHIVED = "archived"
    """
    pass
