"""Module defining the base class for aggregate roots in the domain layer.

An aggregate root is a cluster of domain objects that can be treated as a single unit.
It is responsible for maintaining consistency and enforcing invariants within the aggregate.
The aggregate root is the only entry point for modifying the aggregate.

This module provides the base class `AggregateRoot` that can be inherited to create
custom aggregate roots. Aggregate roots typically contain entities, value objects, and
domain events.
"""

from dataclasses import dataclass, field
from typing import Any
from uuid import UUID

from .interface_domain_event import DomainEvent


@dataclass
class AggregateRoot:
    """Base class for aggregate roots in the domain layer.

    An aggregate root is a cluster of domain objects that can be treated as a single unit.
    It is responsible for maintaining consistency and enforcing invariants within the aggregate.
    The aggregate root is the only entry point for modifying the aggregate.

    Attributes:
        domain_events (list[DomainEvent]): A list of domain events raised by the aggregate root.
    """

    domain_events: list[DomainEvent] = field(default_factory=list, init=False)

    def add_domain_event(self, event: DomainEvent) -> None:
        """Add a domain event to the aggregate root.

        Domain events represent significant changes or actions that occur within the aggregate.
        They are typically used to decouple domain logic and enable event-driven architectures.

        Args:
            event (DomainEvent): The domain event to add.
        """
        self.domain_events.append(event)

    def clear_domain_events(self) -> None:
        """Clear all domain events from the aggregate root.

        This method is typically called after the domain events have been processed.
        """
        self.domain_events.clear()

    def __eq__(self, other: Any) -> bool:
        """Compare two aggregate roots for equality.

        Two aggregate roots are considered equal if they are of the same type and
        have the same unique identifier.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        return self._get_identifier() == other._get_identifier()

    def __hash__(self) -> int:
        """Compute the hash value of the aggregate root.

        The hash value is computed based on the unique identifier of the aggregate root.

        Returns:
            int: The hash value of the aggregate root.
        """
        return hash(self._get_identifier())

    def _get_identifier(self) -> UUID:
        """Get the unique identifier of the aggregate root.

        Subclasses should implement this method to return the unique identifier of the
        aggregate root.

        Returns:
            UUID: The unique identifier of the aggregate root.
        """
        raise NotImplementedError


# Add the class to __all__ for re-export in the parent module.
__all__ = ["AggregateRoot"]
