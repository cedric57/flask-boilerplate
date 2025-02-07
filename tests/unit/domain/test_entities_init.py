"""Unit tests for the domain entities initialization module.
This module contains unit tests to ensure that the `__init__.py` file in the
`flask_boilerplate.domain.entities` package functions correctly. It validates
that entities are properly exported and accessible from the module.
"""

from uuid import UUID

from flask_boilerplate.domain.entities import ExampleEntity


def test_lazy_loading() -> None:
    """Test lazy-loading of entities.

    This test ensures that entities can be dynamically loaded using the
    `__getattr__` function in the `__init__.py` file. It verifies that the
    `ExampleEntity` class is correctly imported and instantiated.
    """
    # Create an instance of ExampleEntity
    entity_id = UUID("12345678-1234-5678-1234-567812345678")
    name = "Test Entity"
    description = "This is a test entity."

    entity = ExampleEntity(id=entity_id, name=name, description=description)

    assert entity.id == entity_id
    assert entity.name == name
    assert entity.description == description


def test_module_exports() -> None:
    """Test module-level exports.

    This test ensures that the `__all__` list in the `__init__.py` file correctly
    defines the entities that are exported by the module. It checks that
    `ExampleEntity` is included in the exported names.
    """
    # Verify that ExampleEntity is accessible from the module
    assert "ExampleEntity" in globals(), "ExampleEntity should be exported by the module."


def test_invalid_entity_access() -> None:
    """Test access to non-existent entities.

    This test ensures that attempting to access an entity that is not defined
    in the `__all__` list raises an appropriate `AttributeError`.
    """
    try:
        # Simulate accessing a non-existent entity
        entity_name = "NonExistentEntity"
        module = __import__("flask_boilerplate.domain.entities")
        getattr(module.domain.entities, entity_name)
        raise AssertionError("Accessing a non-existent entity should raise an AttributeError.")
    except AttributeError as e:
        # Verify the error message
        assert str(e) == "module 'flask_boilerplate.domain.entities' has no attribute 'NonExistentEntity'"


def test_getattr_invalid_name_type() -> None:
    """Test that __getattr__ raises a TypeError when name is not a string."""
    try:
        # Call __getattr__ with an invalid type (e.g., an integer)
        from flask_boilerplate.domain.entities import __getattr__

        __getattr__(123)  # Pass a non-string value
        raise AssertionError("__getattr__ should raise a TypeError for non-string names.")
    except TypeError as e:
        # Verify the error message
        assert str(e) == "Expected a string for entity name, got int"


def test_getattr_dynamic_loading() -> None:
    """Test that __getattr__ dynamically loads and returns an existing entity."""
    # Access an existing entity
    from flask_boilerplate.domain.entities import ExampleEntity

    # Verify that the returned object is the expected class
    assert ExampleEntity.__name__ == "ExampleEntity", "__getattr__ did not return the correct entity."
