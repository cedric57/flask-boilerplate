"""Module for exporting primitive domain constructs.

This module serves as the entry point for all primitive domain constructs, such as
value objects, specifications, repositories, domain events, and aggregate roots.
It re-exports these constructs to make them easily accessible from a single location.

Example:
    >>> from flask_boilerplate.domain.primitives import ValueObject, Specification, Repository
    >>> class MyValueObject(ValueObject):
    ...     pass
"""

from typing import Any

from .aggregate_root import AggregateRoot
from .domain_service import DomainService
from .interface_domain_event import DomainEvent, DomainEventBase
from .repository import Repository, UnitOfWork
from .specification import AndSpecification, NotSpecification, OrSpecification, Specification
from .value_object import ValueObject

# Re-export all primitive domain constructs for easy access.
__all__ = [
    "ValueObject",
    "Specification",
    "AndSpecification",
    "OrSpecification",
    "NotSpecification",
    "Repository",
    "UnitOfWork",
    "DomainEvent",
    "DomainEventBase",
    "AggregateRoot",
    "DomainService",
]


def __getattr__(name: str) -> Any:
    """Lazy-load primitive domain constructs to avoid circular imports.

    Args:
        name (str): The name of the primitive domain construct to load.

    Returns:
        Any: The requested primitive domain construct.

    Raises:
        AttributeError: If the primitive domain construct does not exist.
    """
    if name in __all__:
        # Dynamically import the primitive domain construct to avoid circular imports.
        module = __import__(f"flask_boilerplate.domain.primitives.{name}", fromlist=[name])
        return getattr(module, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
