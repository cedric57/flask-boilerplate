"""Unit tests for domain entities.

This module contains unit tests for the entities in the domain layer. Entities are
domain objects that have a unique identity and lifecycle. They encapsulate business
logic related to their identity and state.

Tests in this module ensure that entities behave as expected and enforce their
invariants.
"""

from uuid import UUID

from flask_boilerplate.domain.entities import ExampleEntity


def test_example_entity_creation() -> None:
    """Test the creation of an ExampleEntity.

    This test ensures that an ExampleEntity can be created with the correct attributes
    and that the attributes are properly initialized.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity = ExampleEntity(id=entity_id, name=name, description=description)

    assert entity.id == entity_id
    assert entity.name == name
    assert entity.description == description


def test_example_entity_update_name() -> None:
    """Test updating the name of an ExampleEntity.

    This test ensures that the `update_name` method correctly updates the name of the
    entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    new_name = "Updated Entity"

    entity = ExampleEntity(id=entity_id, name=name, description=description)
    entity.update_name(new_name)

    assert entity.name == new_name


def test_example_entity_update_description() -> None:
    """Test updating the description of an ExampleEntity.

    This test ensures that the `update_description` method correctly updates the
    description of the entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    new_description = "This is an updated description."

    entity = ExampleEntity(id=entity_id, name=name, description=description)
    entity.update_description(new_description)

    assert entity.description == new_description


def test_example_entity_equality() -> None:
    """Test the equality of two ExampleEntity instances.

    This test ensures that two ExampleEntity instances are considered equal if they
    have the same unique identifier.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity1 = ExampleEntity(id=entity_id, name=name, description=description)
    entity2 = ExampleEntity(id=entity_id, name=name, description=description)

    assert entity1 == entity2


def test_example_entity_inequality() -> None:
    """Test the inequality of two ExampleEntity instances.

    This test ensures that two ExampleEntity instances are considered unequal if they
    have different unique identifiers.
    """
    entity_id1 = UUID("12345678-1234-5678-1234-567812345678")
    entity_id2 = UUID("87654321-4321-8765-4321-876543218765")
    name = "Test Entity"
    description = "This is a test entity."

    entity1 = ExampleEntity(id=entity_id1, name=name, description=description)
    entity2 = ExampleEntity(id=entity_id2, name=name, description=description)

    assert entity1 != entity2


def test_example_entity_hash() -> None:
    """Test the hash value of an ExampleEntity.

    This test ensures that the hash value of an ExampleEntity is based on its unique
    identifier.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity = ExampleEntity(id=entity_id, name=name, description=description)

    assert hash(entity) == hash(entity_id)


def test_example_entity_to_dict() -> None:
    """Test the to_dict method of an ExampleEntity.
    This test ensures that the `to_dict` method returns a dictionary with the correct
    attributes.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = ExampleEntity(id=entity_id, name=name, description=description)
    expected_dict = {
        "id": str(entity_id),
        "name": name,
        "description": description,
    }
    assert entity.to_dict() == expected_dict


def test_example_entity_validate_valid() -> None:
    """Test the validate method of an ExampleEntity with valid data.
    This test ensures that the `validate` method does not raise any exceptions when
    the entity data is valid.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = ExampleEntity(id=entity_id, name=name, description=description)
    try:
        entity.validate()
    except ValueError as e:
        assert False, f"validate() raised an unexpected ValueError: {e}"


def test_example_entity_validate_invalid_name() -> None:
    """Test the validate method of an ExampleEntity with an invalid name.
    This test ensures that the `validate` method raises a ValueError when the name is
    empty or consists only of whitespace.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "   "
    description = "This is a test entity."
    entity = ExampleEntity(id=entity_id, name=name, description=description)
    try:
        entity.validate()
        assert False, "validate() did not raise ValueError for invalid name"
    except ValueError as e:
        assert str(e) == "Name cannot be empty."


def test_example_entity_validate_invalid_description() -> None:
    """Test the validate method of an ExampleEntity with an invalid description.
    This test ensures that the `validate` method raises a ValueError when the description
    is empty or consists only of whitespace.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "   "
    entity = ExampleEntity(id=entity_id, name=name, description=description)
    try:
        entity.validate()
        assert False, "validate() did not raise ValueError for invalid description"
    except ValueError as e:
        assert str(e) == "Description cannot be empty."


def test_example_entity_default_id() -> None:
    """Test the creation of an ExampleEntity with a default UUID.
    This test ensures that an ExampleEntity can be created without providing an ID,
    and a default UUID is generated.
    """
    name = "Test Entity"
    description = "This is a test entity."
    entity = ExampleEntity(name=name, description=description)
    assert isinstance(entity.id, UUID)
    assert entity.name == name
    assert entity.description == description


def test_example_entity_str_representation() -> None:
    """Test the string representation of an ExampleEntity.
    This test ensures that the `__str__` method returns a meaningful string representation
    of the entity.
    """
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."
    entity = ExampleEntity(id=entity_id, name=name, description=description)
    expected_str = f"ExampleEntity(id={entity_id}, name={name}, description={description})"
    assert str(entity) == expected_str
