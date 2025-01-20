from abc import ABC, abstractmethod
import uuid

class Entity(ABC):
    """
    Base class for all entities in the domain layer.
    
    An entity is an object that is defined by its identity rather than its attributes.
    Entities have a unique identifier and can be compared based on this identifier.
    
    Attributes:
        id (uuid.UUID): The unique identifier of the entity.
    """
    
    def __init__(self, id: uuid.UUID = None):
        """
        Initialize a new entity with a unique identifier.
        
        Args:
            id (uuid.UUID, optional): The unique identifier of the entity. If not provided, a new UUID is generated.
        """
        self.id = id or uuid.uuid4()
    
    @abstractmethod
    def __eq__(self, other):
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
    
    def __hash__(self):
        """
        Generate a hash value for the entity based on its unique identifier.
        
        Returns:
            int: The hash value of the entity.
        """
        return hash(self.id)
