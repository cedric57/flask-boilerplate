"""Module defining the base interfaces for repositories in the domain layer.

Repositories are used to abstract the persistence and retrieval of domain objects.
They provide a collection-like interface for accessing domain objects while hiding
the details of the underlying data storage.

This module provides the base interfaces `Repository` and `UnitOfWork` that can be
implemented to create custom repositories and transaction management mechanisms.
"""

from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Generic, Optional, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


class Repository(Generic[T, ID], ABC):
    """Base interface for repositories in the domain layer.

    A repository provides a collection-like interface for accessing domain objects.
    It abstracts the details of data storage and retrieval, allowing the domain layer
    to remain agnostic of the underlying persistence mechanism.

    Subclasses should implement the methods to provide specific persistence logic.

    Example:
        >>> class UserRepository(Repository[User, UUID]):
        ...     def add(self, user: User) -> None:
        ...         pass
        ...
        ...     def get(self, user_id: UUID) -> Optional[User]:
        ...         pass
        ...
        ...     def list(self) -> Iterable[User]:
        ...         pass
        ...
        ...     def remove(self, user: User) -> None:
        ...         pass
    """

    @abstractmethod
    def add(self, entity: T) -> None:
        """Add a new entity to the repository.

        Args:
            entity (T): The entity to add.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, id: ID) -> Optional[T]:
        """Retrieve an entity by its unique identifier.

        Args:
            id (ID): The unique identifier of the entity.

        Returns:
            Optional[T]: The entity if found, otherwise None.
        """
        raise NotImplementedError

    @abstractmethod
    def list(self) -> Iterable[T]:
        """Retrieve all entities from the repository.

        Returns:
            Iterable[T]: A collection of all entities.
        """
        raise NotImplementedError

    @abstractmethod
    def remove(self, entity: T) -> None:
        """Remove an entity from the repository.

        Args:
            entity (T): The entity to remove.
        """
        raise NotImplementedError


class UnitOfWork(Generic[T, ID], ABC):
    """Base interface for the Unit of Work pattern in the domain layer.

    The Unit of Work pattern is used to manage transactions and track changes to
    domain objects. It ensures that all changes are committed or rolled back as
    a single unit.

    Subclasses should implement the methods to provide specific transaction management.

    Example:
        >>> class UserUnitOfWork(UnitOfWork[User, UUID]):
        ...     def commit(self) -> None:
        ...         pass
        ...
        ...     def rollback(self) -> None:
        ...         pass
        ...
        ...     def repositories(self) -> dict[str, Repository[User, UUID]]:
        ...         pass
    """

    @abstractmethod
    def commit(self) -> None:
        """Commit all changes made within the unit of work."""
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        """Roll back all changes made within the unit of work."""
        raise NotImplementedError

    @abstractmethod
    def repositories(self) -> dict[str, Repository[T, ID]]:
        """Get the repositories managed by this unit of work.

        Returns:
            dict[str, Repository[T, ID]]: A dictionary of repositories, keyed by name.
        """
        raise NotImplementedError


# Add the classes to __all__ for re-export in the parent module.
__all__ = ["Repository", "UnitOfWork"]
