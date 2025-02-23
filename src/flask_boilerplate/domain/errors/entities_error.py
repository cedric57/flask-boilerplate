class EntitiesError(Exception):
    """Base class for exceptions related to Entities in the domain layer.

    This class serves as the base exception for all entity-related errors
    within the domain layer. By inheriting from the built-in `Exception` class,
    it provides a consistent way to handle and propagate entity errors.

    Attributes:
        message (str): The error message describing the issue.
    """

    def __init__(self, message: str) -> None:
        """Initialize a new EntitiesError with a specific message.

        Args:
            message (str): The error message describing the issue.
        """
        super().__init__(message)
