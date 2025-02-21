"""Module defining the base class for value objects in the domain layer.

Value objects are immutable objects that are defined by their attributes rather than
a unique identity. They encapsulate domain-specific logic and ensure consistency
and validity of data within the domain.

This module provides a base class `ValueObject` that can be inherited to create
custom value objects. Value objects are compared based on their attributes rather
than their identity.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any

from flask_boilerplate.domain.errors import ValueObjectsError


@dataclass(frozen=True)
class ValueObject(ABC):
    """Abstract base class for all value objects in the domain layer.

    A value object is an immutable object that is defined by its attributes.
    It does not have a unique identity and is compared based on its attribute values.

    Implements core value object characteristics:
    - Immutability
    - Structural equality
    - Validation
    - Serialization/deserialization

    Subclasses should define their attributes using dataclass fields. The `frozen=True`
    parameter ensures immutability.

    Inheriting classes must implement:
    - _validate() method
    - to_primitives() method

    Example:
        >>> @dataclass(frozen=True)
        >>> class Money(ValueObject):
        ...     amount: float
        ...     currency: str
        ...
        >>> money1 = Money(amount=100.0, currency="USD")
        >>> money2 = Money(amount=100.0, currency="USD")
        >>> money1 == money2
        True
    """

    def __post_init__(self) -> None:
        """
        Post-initialization hook to ensure the value object is properly validated.
        """
        self.validate()

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Compare two value objects based on their attributes.
        Args:
            other (Any): The other value object to compare with.
        Returns:
            bool: True if the value objects have the same attributes, False otherwise.
        """
        if not isinstance(other, ValueObject):
            return False
        return self._attributes() == other._attributes()

    @abstractmethod
    def __hash__(self) -> int:
        """
        Generate a hash value for the value object based on its attributes.
        Returns:
            int: The hash value of the value object.
        """
        return hash(self._attributes())

    @abstractmethod
    def _attributes(self) -> tuple[Any, ...]:
        """
        Get the attributes of the value object for comparison and hashing.
        Returns:
            tuple[Any, ...]: A tuple of the value object's attributes.
        """
        pass

    def validate(self) -> None:
        """
        Validate the value object's data.
        Raises:
            ValueObjectsError: If the value object's data is invalid.
        """
        if not self._attributes():
            raise ValueObjectsError("Value object attributes cannot be empty.")


# Add the class to __all__ for re-export in the parent module.
__all__ = ["ValueObject"]
