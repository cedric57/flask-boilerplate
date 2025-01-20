from abc import ABC, abstractmethod

class DomainService(ABC):
    """
    Base class for domain services in the domain layer.
    
    A domain service encapsulates business logic that does not naturally fit within an entity or value object.
    """
    
    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute the domain service logic.
        
        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        
        Returns:
            Any: The result of the domain service execution.
        """
        pass
