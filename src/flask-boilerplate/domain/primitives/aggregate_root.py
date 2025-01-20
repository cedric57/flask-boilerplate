from .entity import Entity

class AggregateRoot(Entity):
    """
    Base class for aggregate roots in the domain layer.
    
    An aggregate root is an entity that serves as the entry point for an aggregate.
    Aggregates are clusters of domain objects that can be treated as a single unit.
    The aggregate root ensures the consistency of changes being made within the aggregate.
    
    Attributes:
        id (uuid.UUID): The unique identifier of the aggregate root.
    """
    
    def __init__(self, id=None):
        """
        Initialize a new aggregate root with a unique identifier.
        
        Args:
            id (uuid.UUID, optional): The unique identifier of the aggregate root. If not provided, a new UUID is generated.
        """
        super().__init__(id)
    
    def add_domain_event(self, event):
        """
        Add a domain event to the aggregate root.
        
        Args:
            event (DomainEvent): The domain event to add.
        """
        if not hasattr(self, '_domain_events'):
            self._domain_events = []
        self._domain_events.append(event)
    
    def clear_domain_events(self):
        """
        Clear all domain events from the aggregate root.
        """
        self._domain_events = []
    
    def get_domain_events(self):
        """
        Get all domain events from the aggregate root.
        
        Returns:
            list: A list of domain events.
        """
        return getattr(self, '_domain_events', [])
