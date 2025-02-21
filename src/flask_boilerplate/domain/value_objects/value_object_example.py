from dataclasses import dataclass
from typing import Any

from flask_boilerplate.domain.errors.value_objects_error import ValueObjectsError
from flask_boilerplate.domain.primitives.value_object import ValueObject


@dataclass(frozen=True)
class ValueObjectExample(ValueObject):
    """
    An example value object in the domain layer.
    This value object represents a domain object with attributes that define its state.
    It encapsulates business logic related to its attributes.

    Attributes:
        name (str): The name of the value object.
        description (str): A description of the value object.
    """

    name: str
    description: str

    def _attributes(self) -> tuple[Any, ...]:
        """
        Get the attributes of the value object for comparison and hashing.

        Returns:
            tuple[Any, ...]: A tuple of the value object's attributes.
        """
        return self.name, self.description

    def __eq__(self, other: Any) -> bool:
        """
        Compare two value objects based on their attributes.

        Args:
            other (Any): The other value object to compare with.

        Returns:
            bool: True if the value objects have the same attributes, False otherwise.
        """
        if not isinstance(other, ValueObjectExample):
            return NotImplemented
        return self._attributes() == other._attributes()

    def __hash__(self) -> int:
        """
        Generate a hash value for the value object based on its attributes.

        Returns:
            int: The hash value of the value object.
        """
        return hash(self._attributes())

    def validate(self) -> None:
        """
        Validate the value object's data.

        Raises:
            ValueObjectsError: If the value object's data is invalid.
        """
        if not self.name or len(self.name.strip()) == 0:
            raise ValueObjectsError("Name cannot be empty.")
        if not self.description or len(self.description.strip()) == 0:
            raise ValueObjectsError("Description cannot be empty.")
