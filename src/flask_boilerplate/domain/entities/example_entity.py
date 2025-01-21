from src.flask_boilerplate.domain.primitives.entity import Entity
from typing import Any
import uuid


class ExampleEntity(Entity):
    """
    ExampleEntity represents a sample entity in the domain layer.

    This entity is defined by its unique identifier and includes additional attributes
    that represent its state.

    Attributes:
        id (uuid.UUID): The unique identifier of the entity.
        name (str): The name of the entity.
        value (int): A sample value associated with the entity.
    """

    def __init__(self, id: uuid.UUID = None, name: str = "", value: int = 0) -> None:
        """
        Initialize a new ExampleEntity with a unique identifier, name, and value.

        Args:
            id (Optional[uuid.UUID]): The unique identifier of the entity. If not provided, a new UUID is generated.
            name (str): The name of the entity.
            value (int): A sample value associated with the entity.
        """
        super().__init__(id)
        self.name: str = name
        self.value: int = value

    def __eq__(self, other: Any) -> bool:
        """
        Compare two entities based on their unique identifier and attributes.

        Args:
            other (Any): The other entity to compare with.

        Returns:
            bool: True if the entities have the same identifier and attributes, False otherwise.
        """
        if not isinstance(other, ExampleEntity):
            return False
        return self.id == other.id and self.name == other.name and self.value == other.value

    def __hash__(self) -> int:
        """
        Generate a hash value for the entity based on its unique identifier and attributes.

        Returns:
            int: The hash value of the entity.
        """
        return hash((self.id, self.name, self.value))
