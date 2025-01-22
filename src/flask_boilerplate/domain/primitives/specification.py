"""Module defining the base class for specifications in the domain layer.

Specifications are used to encapsulate business rules or conditions that can be
used to filter, query, or validate domain objects. They follow the Specification
pattern, which allows for reusable and composable business logic.

This module provides a base class `Specification` that can be inherited to create
custom specifications. Specifications can be combined using logical operators
(`&`, `|`, `~`) to create complex conditions.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Specification(ABC, Generic[T]):
    """Base class for specifications in the domain layer.

    A specification encapsulates a business rule or condition that can be evaluated
    against a domain object. It follows the Specification pattern, allowing for
    reusable and composable business logic.

    Subclasses should implement the `is_satisfied_by` method to define the specific
    condition or rule.

    Example:
        >>> class IsActiveSpecification(Specification[User]):
        ...     def is_satisfied_by(self, user: User) -> bool:
        ...         return user.is_active
        ...
        >>> active_spec = IsActiveSpecification()
        >>> user = User(is_active=True)
        >>> active_spec.is_satisfied_by(user)
        True
    """

    @abstractmethod
    def is_satisfied_by(self, candidate: T) -> bool:
        """Check if the candidate satisfies the specification.

        Args:
            candidate (T): The domain object to evaluate.

        Returns:
            bool: True if the candidate satisfies the specification, False otherwise.
        """
        raise NotImplementedError

    def __and__(self, other: "Specification[T]") -> "AndSpecification[T]":
        """Combine two specifications using the logical AND operator.

        Args:
            other (Specification[T]): The other specification to combine with.

        Returns:
            AndSpecification[T]: A new specification representing the logical AND.
        """
        return AndSpecification(self, other)

    def __or__(self, other: "Specification[T]") -> "OrSpecification[T]":
        """Combine two specifications using the logical OR operator.

        Args:
            other (Specification[T]): The other specification to combine with.

        Returns:
            OrSpecification[T]: A new specification representing the logical OR.
        """
        return OrSpecification(self, other)

    def __invert__(self) -> "NotSpecification[T]":
        """Negate the specification using the logical NOT operator.

        Returns:
            NotSpecification[T]: A new specification representing the logical NOT.
        """
        return NotSpecification(self)


class AndSpecification(Specification[T]):
    """Specification representing the logical AND of two specifications."""

    def __init__(self, first: Specification[T], second: Specification[T]) -> None:
        """Initialize the AndSpecification.

        Args:
            first (Specification[T]): The first specification.
            second (Specification[T]): The second specification.
        """
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate: T) -> bool:
        """Check if the candidate satisfies both specifications.

        Args:
            candidate (T): The domain object to evaluate.

        Returns:
            bool: True if the candidate satisfies both specifications, False otherwise.
        """
        return self.first.is_satisfied_by(candidate) and self.second.is_satisfied_by(candidate)


class OrSpecification(Specification[T]):
    """Specification representing the logical OR of two specifications."""

    def __init__(self, first: Specification[T], second: Specification[T]) -> None:
        """Initialize the OrSpecification.

        Args:
            first (Specification[T]): The first specification.
            second (Specification[T]): The second specification.
        """
        self.first = first
        self.second = second

    def is_satisfied_by(self, candidate: T) -> bool:
        """Check if the candidate satisfies at least one of the specifications.

        Args:
            candidate (T): The domain object to evaluate.

        Returns:
            bool: True if the candidate satisfies at least one specification, False otherwise.
        """
        return self.first.is_satisfied_by(candidate) or self.second.is_satisfied_by(candidate)


class NotSpecification(Specification[T]):
    """Specification representing the logical NOT of a specification."""

    def __init__(self, specification: Specification[T]) -> None:
        """Initialize the NotSpecification.

        Args:
            specification (Specification[T]): The specification to negate.
        """
        self.specification = specification

    def is_satisfied_by(self, candidate: T) -> bool:
        """Check if the candidate does not satisfy the specification.

        Args:
            candidate (T): The domain object to evaluate.

        Returns:
            bool: True if the candidate does not satisfy the specification, False otherwise.
        """
        return not self.specification.is_satisfied_by(candidate)


# Add the classes to __all__ for re-export in the parent module.
__all__ = ["Specification", "AndSpecification", "OrSpecification", "NotSpecification"]
