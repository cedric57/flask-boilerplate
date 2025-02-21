from flask_boilerplate.domain.errors.value_objects_error import ValueObjectsError
from flask_boilerplate.domain.value_objects.value_object_example import ValueObjectExample


def test_value_object_example_creation() -> None:
    """Test the creation of a ValueObjectExample."""
    name = "Test Value Object"
    description = "This is a test value object."
    value_object = ValueObjectExample(name=name, description=description)
    assert value_object.name == name
    assert value_object.description == description


def test_value_object_example_equality() -> None:
    """Test the equality of two ValueObjectExample instances."""
    name = "Test Value Object"
    description = "This is a test value object."
    value_object1 = ValueObjectExample(name=name, description=description)
    value_object2 = ValueObjectExample(name=name, description=description)
    assert value_object1 == value_object2


def test_value_object_example_equality_not_implemented() -> None:
    """Test that __eq__ returns NotImplemented for non-ValueObjectExample objects."""
    name = "Test Value Object"
    description = "This is a test value object."
    value_object = ValueObjectExample(name=name, description=description)
    other_object = "Not a ValueObjectExample"
    assert value_object.__eq__(other_object) is NotImplemented, (
        "__eq__ should return NotImplemented for non-ValueObjectExample objects."
    )


def test_value_object_example_inequality() -> None:
    """Test the inequality of two ValueObjectExample instances."""
    name1 = "Test Value Object 1"
    description1 = "This is a test value object 1."
    name2 = "Test Value Object 2"
    description2 = "This is a test value object 2."
    value_object1 = ValueObjectExample(name=name1, description=description1)
    value_object2 = ValueObjectExample(name=name2, description=description2)
    assert value_object1 != value_object2


def test_value_object_example_hash() -> None:
    """Test the hash value of a ValueObjectExample."""
    name = "Test Value Object"
    description = "This is a test value object."
    value_object = ValueObjectExample(name=name, description=description)
    assert hash(value_object) == hash((name, description))


def test_value_object_example_validate_valid() -> None:
    """Test the validate method of a ValueObjectExample with valid data."""
    name = "Test Value Object"
    description = "This is a test value object."
    value_object = ValueObjectExample(name=name, description=description)
    try:
        value_object.validate()
    except ValueObjectsError as e:
        raise AssertionError(f"validate() raised an unexpected ValueObjectsError: {e}") from None


def test_value_object_example_validate_invalid_name() -> None:
    """Test the validate method of a ValueObjectExample with an invalid name."""
    name = "   "
    description = "This is a test value object."
    try:
        ValueObjectExample(name=name, description=description)
        raise AssertionError("validate() did not raise ValueObjectsError for invalid name")
    except ValueObjectsError as e:
        assert str(e) == "Name cannot be empty."


def test_value_object_example_validate_invalid_description() -> None:
    """Test the validate method of a ValueObjectExample with an invalid description."""
    name = "Test Value Object"
    description = "   "
    try:
        ValueObjectExample(name=name, description=description)
        raise AssertionError("validate() did not raise ValueObjectsError for invalid description")
    except ValueObjectsError as e:
        assert str(e) == "Description cannot be empty."
