from abc import ABC, abstractmethod


class ValueObject(ABC):
    """
    Base class for all value objects in the domain layer.

    A value object is an immutable type that is distinguishable only by the state of its properties.
    Value objects do not have an identity and are compared based on their properties.
    """

    @abstractmethod
    def __eq__(self, other):
        """
        Compare two value objects based on their properties.

        Args:
            other (ValueObject): The other value object to compare with.

        Returns:
            bool: True if the value objects have the same properties, False otherwise.
        """
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Compare two value objects to determine if they are not equal.

        Args:
            other (ValueObject): The other value object to compare with.

        Returns:
            bool: True if the value objects do not have the same properties, False otherwise.
        """
        return not self.__eq__(other)

    def __hash__(self):
        """
        Generate a hash value for the value object based on its properties.

        Returns:
            int: The hash value of the value object.
        """
        return hash(tuple(sorted(self.__dict__.items())))
