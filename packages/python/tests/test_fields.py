import uuid
from datetime import datetime

import pytest
from pydantic import BaseModel, ValidationError

from quanttide import (
    CreatedAtField,
    DescriptionField,
    IdField,
    LabelField,
    NameField,
    OrderField,
    TitleField,
    UpdatedAtField,
)


def _make(field_type, value):
    class M(BaseModel):
        f: field_type

    return M(f=value).f


class TestIdField:
    def test_accepts_uuid(self):
        val = uuid.uuid4()
        assert _make(IdField, val) == val

    def test_accepts_uuid_str(self):
        val = "00000000-0000-0000-0000-000000000001"
        assert _make(IdField, val) == uuid.UUID(val)

    def test_rejects_invalid_uuid(self):
        with pytest.raises(ValidationError):
            _make(IdField, "not-a-uuid")


class TestNameField:
    def test_accepts_valid_name(self):
        assert _make(NameField, "my-project") == "my-project"

    def test_rejects_too_long(self):
        with pytest.raises(ValidationError):
            _make(NameField, "a" * 101)


class TestOrderField:
    def test_accepts_positive(self):
        assert _make(OrderField, 1) == 1

    def test_rejects_zero(self):
        with pytest.raises(ValidationError):
            _make(OrderField, 0)

    def test_rejects_negative(self):
        with pytest.raises(ValidationError):
            _make(OrderField, -1)


class TestLabelField:
    def test_accepts_label(self):
        assert _make(LabelField, "Active") == "Active"

    def test_rejects_too_long(self):
        with pytest.raises(ValidationError):
            _make(LabelField, "a" * 51)


class TestTitleField:
    def test_accepts_title(self):
        assert _make(TitleField, "My Project") == "My Project"

    def test_rejects_too_long(self):
        with pytest.raises(ValidationError):
            _make(TitleField, "a" * 256)


class TestDescriptionField:
    def test_accepts_description(self):
        assert _make(DescriptionField, "some long text") == "some long text"


class TestCreatedAtField:
    def test_accepts_datetime(self):
        val = datetime.now()
        assert _make(CreatedAtField, val) == val


class TestUpdatedAtField:
    def test_accepts_datetime(self):
        val = datetime.now()
        assert _make(UpdatedAtField, val) == val
