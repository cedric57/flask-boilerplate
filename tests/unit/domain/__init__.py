"""Module for exporting unit tests for the domain layer.

This module serves as the entry point for all unit tests related to the domain layer.
It re-exports test modules to make them easily accessible from a single location.

Unit tests in this module ensure that domain objects (e.g., entities, value objects,
aggregate roots) behave as expected and enforce their invariants.
"""

from typing import Any

# Re-export all unit test modules for easy access.
__all__: list[str] = []


def __getattr__(name: str) -> Any:
    """Lazy-load unit test modules to avoid circular imports.

    Args:
        name (str): The name of the unit test module to load.

    Returns:
        Any: The requested unit test module.

    Raises:
        AttributeError: If the unit test module does not exist.
    """
    if name in __all__:
        # Dynamically import the unit test module to avoid circular imports.
        module = __import__(f"tests.unit.domain.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
