"""
This package contains the base types and interfaces used in the domain layer.

The primitives package includes foundational classes such as entities, value objects,
aggregate roots, and domain events, which are essential for building the domain logic.
"""

# Import necessary base classes and interfaces for the domain layer
from .aggregate_root import AggregateRoot as AggregateRoot
from .entity import Entity as Entity
from .interface_domain_event import DomainEvent as DomainEvent
from .value_object import ValueObject as ValueObject
