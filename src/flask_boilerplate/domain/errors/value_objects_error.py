class ValueObjectsError(Exception):
    """Base class for exceptions related to Value Objects in the domain layer.

    This class serves as the base exception for all value object-related errors
    within the domain layer. By inheriting from the built-in `Exception` class,
    it provides a consistent way to handle and propagate value object errors.

    Attributes:
        message (str): The error message describing the issue.
    """

    def __init__(self, message: str) -> None:
        """Initialize a new ValueObjectsError with a specific message.

        Args:
            message (str): The error message describing the issue.
        """
        super().__init__(message)
