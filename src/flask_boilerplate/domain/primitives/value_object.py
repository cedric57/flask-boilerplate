"""Module defining the base class for value objects in the domain layer.

Value objects are immutable objects that are defined by their attributes rather than
a unique identity. They encapsulate domain-specific logic and ensure consistency
and validity of data within the domain.

This module provides a base class `ValueObject` that can be inherited to create
custom value objects. Value objects are compared based on their attributes rather
than their identity.
"""

from dataclasses import dataclass, fields
from typing import Any


@dataclass(frozen=True)
class ValueObject:
    """Base class for value objects in the domain layer.

    A value object is an immutable object that is defined by its attributes.
    It does not have a unique identity and is compared based on its attribute values.

    Subclasses should define their attributes using dataclass fields. The `frozen=True`
    parameter ensures immutability.

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

    def __eq__(self, other: Any) -> bool:
        """Compare two value objects for equality.

        Two value objects are considered equal if they are of the same type and
        all their attributes have the same values.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        return self._get_attributes() == other._get_attributes()

    def __hash__(self) -> int:
        """Compute the hash value of the value object.

        The hash value is computed based on the values of the object's attributes.

        Returns:
            int: The hash value of the object.
        """
        return hash(self._get_attributes())

    def _get_attributes(self) -> tuple[Any, ...]:
        """Get the values of all attributes of the value object.

        Returns:
            tuple[Any, ...]: A tuple containing the values of all attributes.
        """
        return tuple(getattr(self, field.name) for field in fields(self))

    def to_dict(self) -> dict[str, Any]:
        """Convert the value object to a dictionary.

        Returns:
            dict[str, Any]: A dictionary representation of the value object.
        """
        return {field.name: getattr(self, field.name) for field in fields(self)}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "ValueObject":
        """Create a value object from a dictionary.

        Args:
            data (dict[str, Any]): A dictionary containing the attribute values.

        Returns:
            ValueObject: A new instance of the value object.

        Raises:
            ValueError: If the dictionary contains invalid or missing attributes.
        """
        field_names = {field.name for field in fields(cls)}
        invalid_keys = set(data.keys()) - field_names
        if invalid_keys:
            raise ValueError(f"Invalid keys for {cls.__name__}: {invalid_keys}")
        return cls(**{key: data[key] for key in field_names if key in data})


# Add the class to __all__ for re-export in the parent module.
__all__ = ["ValueObject"]
