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
