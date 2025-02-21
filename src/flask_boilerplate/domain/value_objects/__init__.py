"""Module for exporting value objects in the domain layer.

This module serves as the entry point for all value objects in the domain layer. It re-exports
value objects to make them easily accessible from a single location.

Value objects are domain objects that are defined by their attributes rather than their identity.
They are immutable and can be compared based on their attributes.

Example:
    >>> from flask_boilerplate.domain.value_objects import ValueObjectExample
    >>> value_object = ValueObjectExample(name="Example", description="An example value object")
    >>> print(value_object.attribute1)
    "value1"
"""

import logging
from typing import Any

from .value_object_example import ValueObjectExample

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Re-export all value objects for easy access.
__all__ = [
    "ValueObjectExample",
]


def __getattr__(name: str) -> Any:
    """Lazy-load value objects to avoid circular imports.

    Args:
        name (str): The name of the value object to load.

    Returns:
        Any: The requested value object.

    Raises:
        AttributeError: If the value object does not exist.
    """
    if not isinstance(name, str):
        raise TypeError(f"Expected a string for value object name, got {type(name).__name__}")
    if name in __all__:
        logger.debug(f"Lazy-loading value object: {name}")
        # Dynamically import the value object to avoid circular imports.
        module = __import__(f"flask_boilerplate.domain.value_objects.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
