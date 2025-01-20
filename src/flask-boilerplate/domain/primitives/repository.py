from abc import ABC, abstractmethod

class Repository(ABC):
    """
    Interface for repositories in the domain layer.
    
    A repository provides methods for accessing aggregates and entities.
    """
    
    @abstractmethod
    def add(self, entity):
        """
        Add an entity to the repository.
        
        Args:
            entity (Entity): The entity to add.
        """
        pass
    
    @abstractmethod
    def get_by_id(self, entity_id):
        """
        Retrieve an entity by its unique identifier.
        
        Args:
            entity_id (uuid.UUID): The unique identifier of the entity.
        
        Returns:
            Entity: The retrieved entity.
        """
        pass
    
    @abstractmethod
    def remove(self, entity):
        """
        Remove an entity from the repository.
        
        Args:
            entity (Entity): The entity to remove.
        """
        pass
