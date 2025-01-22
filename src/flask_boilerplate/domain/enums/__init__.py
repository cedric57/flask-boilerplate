"""Module for defining enumerations in the domain layer.

Enumerations are used to represent a fixed set of constants or options within the domain.
They provide a type-safe way to work with predefined values and ensure consistency
across the application.

This module serves as the entry point for all enumerations in the domain layer.
It exports the necessary enums to be used across the application.

Example:
    >>> from flask_boilerplate.domain.enums import MyEnum
    >>> my_value = MyEnum.VALUE1
    >>> print(my_value)
    MyEnum.VALUE1
"""

from typing import Any

from .example_enum import ExampleEnum

# Re-export all enums here to make them accessible from this module.
# This allows for a cleaner import structure in other parts of the application.
# Example:
# from .my_enum import MyEnum
# __all__ = ["MyEnum"]

__all__ = ["ExampleEnum"]


def __getattr__(name: str) -> Any:
    """Lazy-load enums to avoid circular imports.

    Args:
        name (str): The name of the enum to load.

    Returns:
        Any: The requested enum.

    Raises:
        AttributeError: If the enum does not exist.
    """
    if name in __all__:
        # Dynamically import the enum to avoid circular imports.
        module = __import__(f"flask_boilerplate.domain.enums.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
