"""Unit tests for domain entities.

This module contains unit tests for the entities in the domain layer. Entities are
domain objects that have a unique identity and lifecycle. They encapsulate business
logic related to their identity and state.

Tests in this module ensure that entities behave as expected and enforce their
invariants.
"""

from uuid import UUID

from flask_boilerplate.domain.entities import EntityExample
from flask_boilerplate.domain.errors.entities_error import EntitiesError


def test_entity_example_creation() -> None:
    """Test the creation of an EntityExample.

    This test ensures that an EntityExample can be created with the correct attributes
    and that the attributes are properly initialized.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity = EntityExample(id=entity_id, name=name, description=description)

    assert entity.id == entity_id
    assert entity.name == name
    assert entity.description == description


def test_entity_example_update_name() -> None:
    """Test updating the name of an EntityExample.

    This test ensures that the `update_name` method correctly updates the name of the
    entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    new_name = "Updated Entity"

    entity = EntityExample(id=entity_id, name=name, description=description)
    entity.update_name(new_name)

    assert entity.name == new_name


def test_entity_example_update_description() -> None:
    """Test updating the description of an EntityExample.

    This test ensures that the `update_description` method correctly updates the
    description of the entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    new_description = "This is an updated description."

    entity = EntityExample(id=entity_id, name=name, description=description)
    entity.update_description(new_description)

    assert entity.description == new_description


def test_entity_example_equality_not_implemented() -> None:
    """Test the __eq__ method when comparing with a non-Entity object."""
    # Arrange
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = EntityExample(id=entity_id, name=name, description=description)

    # Act
    result = entity.__eq__("not an entity")  # Compare with a non-Entity object

    # Assert
    assert result is NotImplemented, "__eq__ should return NotImplemented for non-Entity objects."


def test_entity_example_equality() -> None:
    """Test the equality of two EntityExample instances.

    This test ensures that two EntityExample instances are considered equal if they
    have the same unique identifier.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity1 = EntityExample(id=entity_id, name=name, description=description)
    entity2 = EntityExample(id=entity_id, name=name, description=description)

    assert entity1 == entity2


def test_entity_example_inequality() -> None:
    """Test the inequality of two EntityExample instances.

    This test ensures that two EntityExample instances are considered unequal if they
    have different unique identifiers.
    """
    entity_id1 = UUID("12345678-1234-5678-1234-567812345678")
    entity_id2 = UUID("87654321-4321-8765-4321-876543218765")
    name = "Test Entity"
    description = "This is a test entity."

    entity1 = EntityExample(id=entity_id1, name=name, description=description)
    entity2 = EntityExample(id=entity_id2, name=name, description=description)

    assert entity1 != entity2


def test_entity_example_hash() -> None:
    """Test the hash value of an EntityExample.

    This test ensures that the hash value of an EntityExample is based on its unique
    identifier.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity = EntityExample(id=entity_id, name=name, description=description)

    assert hash(entity) == hash(entity_id)


def test_entity_example_to_dict() -> None:
    """Test the to_dict method of an EntityExample.
    This test ensures that the `to_dict` method returns a dictionary with the correct
    attributes.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = EntityExample(id=entity_id, name=name, description=description)
    expected_dict = {
        "id": str(entity_id),
        "name": name,
        "description": description,
    }
    assert entity.to_dict() == expected_dict


def test_entity_example_validate_valid() -> None:
    """Test the validate method of an EntityExample with valid data.
    This test ensures that the `validate` method does not raise any exceptions when
    the entity data is valid.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = EntityExample(id=entity_id, name=name, description=description)
    try:
        entity.validate()
    except EntitiesError as e:
        assert False, f"validate() raised an unexpected ValueError: {e}"


def test_entity_example_validate_invalid_name() -> None:
    """Test the validate method of an EntityExample with an invalid name.
    This test ensures that the `validate` method raises a ValueError when the name is
    empty or consists only of whitespace.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "   "
    description = "This is a test entity."
    entity = EntityExample(id=entity_id, name=name, description=description)
    try:
        entity.validate()
        assert False, "validate() did not raise ValueError for invalid name"
    except EntitiesError as e:
        assert str(e) == "Name cannot be empty."


def test_entity_example_validate_invalid_description() -> None:
    """Test the validate method of an EntityExample with an invalid description.
    This test ensures that the `validate` method raises a ValueError when the description
    is empty or consists only of whitespace.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "   "
    entity = EntityExample(id=entity_id, name=name, description=description)
    try:
        entity.validate()
        assert False, "validate() did not raise ValueError for invalid description"
    except EntitiesError as e:
        assert str(e) == "Description cannot be empty."


def test_entity_example_default_id() -> None:
    """Test the creation of an EntityExample with a default UUID.
    This test ensures that an EntityExample can be created without providing an ID,
    and a default UUID is generated.
    """
    name = "Test Entity"
    description = "This is a test entity."
    entity = EntityExample(name=name, description=description)
    assert isinstance(entity.id, UUID)
    assert entity.name == name
    assert entity.description == description


def test_entity_example_str_representation() -> None:
    """Test the string representation of an EntityExample.
    This test ensures that the `__str__` method returns a meaningful string representation
    of the entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = EntityExample(id=entity_id, name=name, description=description)
    expected_str = f"EntityExample(id={entity_id}, name={name}, description={description})"
    assert str(entity) == expected_str
