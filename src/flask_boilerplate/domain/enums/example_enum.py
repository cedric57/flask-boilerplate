"""Example enumeration for the domain layer.

This module defines an example enumeration to demonstrate how to create and use
enums within the domain layer. Enums are useful for representing a fixed set of
constants or options in a type-safe manner.

Example:
    >>> from flask_boilerplate.domain.enums.exemple_enum import ExampleEnum
    >>> status = ExampleEnum.ACTIVE
    >>> print(status)
    ExampleEnum.ACTIVE
"""

from enum import Enum


class ExampleEnum(Enum):
    """Example enumeration for the domain layer.

    This enum represents a set of predefined states or options that can be used
    within the domain logic. Each member of the enum is a constant with a unique value.

    Attributes:
        ACTIVE: Represents an active state.
        INACTIVE: Represents an inactive state.
        PENDING: Represents a pending state.
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

    def __str__(self) -> str:
        """Return the string representation of the enum member.

        Returns:
            str: The string representation of the enum member.
        """
        return f"{self.__class__.__name__}.{self.name}"


# Add the enum to __all__ for re-export in the parent module.
__all__ = ["ExampleEnum"]
