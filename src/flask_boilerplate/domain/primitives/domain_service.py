"""Module defining the base class for domain services in the domain layer.

Domain services encapsulate business logic that does not naturally fit within
an entity or value object. They are stateless and operate on domain objects to
perform complex operations or enforce business rules.

This module provides the base class `DomainService` that can be inherited to create
custom domain services. Domain services are typically used to orchestrate interactions
between multiple domain objects or external systems.
"""

from abc import ABC, abstractmethod
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class DomainService(ABC, Generic[T]):
    """Base class for domain services in the domain layer.

    A domain service encapsulates business logic that operates on domain objects.
    It is stateless and provides methods to perform complex operations or enforce
    business rules.

    Subclasses should implement the methods to provide specific business logic.

    Example:
        >>> class PaymentService(DomainService[Order]):
        ...     def process_payment(self, order: Order) -> bool:
        ...         # Business logic for processing payment
        ...         pass
    """

    @abstractmethod
    def execute(self, entity: T) -> Any:
        """Execute the domain service logic on the given entity.

        This method encapsulates the core business logic of the domain service.
        It operates on the provided entity and returns the result of the operation.

        Args:
            entity (T): The domain object to operate on.

        Returns:
            Any: The result of the domain service operation.
        """
        raise NotImplementedError


# Add the class to __all__ for re-export in the parent module.
__all__ = ["DomainService"]
