from abc import ABC, abstractmethod

class DomainEvent(ABC):
    """
    Interface for domain events in the domain layer.
    
    A domain event is something that has happened in the domain that is of interest to the business.
    Domain events are used to trigger side effects and communicate between different parts of the domain.
    """
    
    @abstractmethod
    def get_event_name(self) -> str:
        """
        Get the name of the domain event.
        
        Returns:
            str: The name of the domain event.
        """
        pass
    
    @abstractmethod
    def get_event_data(self) -> dict:
        """
        Get the data associated with the domain event.
        
        Returns:
            dict: A dictionary containing the event data.
        """
        pass
