import uuid
from abc import ABC, abstractmethod
from typing import Any, Optional


class Entity(ABC):
    """
    Base class for all entities in the domain layer.

    An entity is an object that is defined by its identity rather than its attributes.
    Entities have a unique identifier and can be compared based on this identifier.

    Attributes:
        id (uuid.UUID): The unique identifier of the entity.
    """

    def __init__(self, id: Optional[uuid.UUID] = None) -> None:
        """
        Initialize a new entity with a unique identifier.

        Args:
            id (Optional[uuid.UUID]): The unique identifier of the entity. If not provided, a new UUID is generated.
        """
        self.id: uuid.UUID = id or uuid.uuid4()

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        """
        Compare two entities based on their unique identifier.

        Args:
            other (Entity): The other entity to compare with.

        Returns:
            bool: True if the entities have the same identifier, False otherwise.
        """
        if not isinstance(other, Entity):
            return False
        return self.id == other.id

    def __hash__(self) -> int:
        """
        Generate a hash value for the entity based on its unique identifier.

        Returns:
            int: The hash value of the entity.
        """
        return hash(self.id)
