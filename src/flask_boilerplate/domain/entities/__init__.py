"""Module for exporting entities in the domain layer.

This module serves as the entry point for all entities in the domain layer. It re-exports
entities to make them easily accessible from a single location.

Entities are domain objects that have a unique identity and lifecycle. They encapsulate
business logic related to their identity and state.

Example:
    >>> from flask_boilerplate.domain.entities import ExampleEntity
    >>> entity = ExampleEntity(id=UUID("..."), name="Example", description="An example entity")
"""

from typing import Any

from .example_entity import ExampleEntity

# Re-export all entities for easy access.
__all__ = [
    "ExampleEntity",
]


def __getattr__(name: str) -> Any:
    """Lazy-load entities to avoid circular imports.

    Args:
        name (str): The name of the entity to load.

    Returns:
        Any: The requested entity.

    Raises:
        AttributeError: If the entity does not exist.
    """
    if name in __all__:
        # Dynamically import the entity to avoid circular imports.
        module = __import__(f"flask_boilerplate.domain.entities.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
