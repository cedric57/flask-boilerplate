"""Module for defining value objects in the domain layer.

Value objects are immutable objects that are defined by their attributes rather than
a unique identity. They are used to encapsulate domain-specific logic and ensure
consistency and validity of data within the domain.

This module serves as the entry point for all value objects in the domain layer.
It exports the necessary classes and functions to be used across the application.

Example:
    >>> from flask_boilerplate.domain.value_objects import MyValueObject
    >>> value_object = MyValueObject(attribute1="value1", attribute2="value2")
    >>> print(value_object.attribute1)
    "value1"
"""

from typing import Any

# Re-export all value objects here to make them accessible from this module.
# This allows for a cleaner import structure in other parts of the application.
# Example:
# from .my_value_object import MyValueObject
# __all__ = ["MyValueObject"]

__all__: list[str] = []


def __getattr__(name: str) -> Any:
    """Lazy-load value objects to avoid circular imports.

    Args:
        name (str): The name of the value object to load.

    Returns:
        Any: The requested value object.

    Raises:
        AttributeError: If the value object does not exist.
    """
    if name in __all__:
        # Dynamically import the value object to avoid circular imports.
        module = __import__(f"flask_boilerplate.domain.value_objects.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
