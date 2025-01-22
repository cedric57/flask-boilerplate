"""Module defining the base interface for domain events in the domain layer.

Domain events are used to represent significant changes or actions that occur within
the domain. They are typically used to decouple domain logic and enable event-driven
architectures.

This module provides the base interface `DomainEvent` that can be implemented to
create custom domain events. Domain events are immutable and should contain all the
information necessary to describe the event.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime


class DomainEvent(ABC):
    """Base interface for domain events in the domain layer.

    A domain event represents a significant change or action that occurs within the
    domain. It is immutable and contains all the information necessary to describe
    the event.

    Subclasses should implement the `event_name` property and any additional attributes
    required to describe the event.

    Example:
        >>> @dataclass(frozen=True)
        >>> class UserRegistered(DomainEvent):
        ...     user_id: str
        ...     email: str
        ...     timestamp: datetime = datetime.now()
        ...
        ...     @property
        ...     def event_name(self) -> str:
        ...         return "user_registered"
    """

    @property
    @abstractmethod
    def event_name(self) -> str:
        """Get the name of the domain event.

        The event name is used to identify the type of event and is typically used
        for routing or logging purposes.

        Returns:
            str: The name of the domain event.
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def timestamp(self) -> datetime:
        """Get the timestamp of when the domain event occurred.

        Returns:
            datetime: The timestamp of the domain event.
        """
        raise NotImplementedError


@dataclass(frozen=True)
class DomainEventBase(DomainEvent):
    """Base implementation of the `DomainEvent` interface.

    This class provides a default implementation for the `timestamp` property and
    can be used as a base class for custom domain events.

    Example:
        >>> @dataclass(frozen=True)
        >>> class UserRegistered(DomainEventBase):
        ...     user_id: str
        ...     email: str
        ...
        ...     @property
        ...     def event_name(self) -> str:
        ...         return "user_registered"
    """

    timestamp: datetime

    @property
    def event_name(self) -> str:
        """Get the name of the domain event.

        This method must be implemented by subclasses to provide the event name.

        Returns:
            str: The name of the domain event.
        """
        raise NotImplementedError


# Add the classes to __all__ for re-export in the parent module.
__all__ = ["DomainEvent", "DomainEventBase"]
