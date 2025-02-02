"""Module defining an example entity in the domain layer.

Entities are domain objects that have a unique identity and lifecycle. They are defined
by their attributes and behavior, and they encapsulate business logic related to their
identity and state.

This module provides an example entity `ExampleEntity` that demonstrates how to define
entities in the domain layer. Entities typically have a unique identifier and attributes
that represent their state.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass
class ExampleEntity:
    """An example entity in the domain layer.

    This entity represents a domain object with a unique identity and attributes.
    It encapsulates business logic related to its identity and state.

    Attributes:
        id (UUID): The unique identifier of the entity.
        name (str): The name of the entity.
        description (str): A description of the entity.
    """

    id: UUID
    name: str
    description: str

    def __hash__(self) -> int:
        return hash(self.id)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExampleEntity):
            return NotImplemented
        return self.id == other.id  # L'égalité se base aussi sur l'UUID

    def update_name(self, new_name: str) -> None:
        """Update the name of the entity.

        Args:
            new_name (str): The new name for the entity.
        """
        self.name = new_name

    def update_description(self, new_description: str) -> None:
        """Update the description of the entity.

        Args:
            new_description (str): The new description for the entity.
        """
        self.description = new_description


# Add the class to __all__ for re-export in the parent module.
__all__ = ["ExampleEntity"]
