"""
This package contains the base types and interfaces used in the domain layer.

The primitives package includes foundational classes such as entities, value objects,
aggregate roots, and domain events, which are essential for building the domain logic.
"""

# Import necessary base classes and interfaces for the domain layer
from .entity import Entity
from .value_object import ValueObject
from .aggregate_root import AggregateRoot
from .interface_domain_event import DomainEvent
