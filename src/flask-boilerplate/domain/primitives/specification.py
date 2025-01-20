from abc import ABC, abstractmethod

class Specification(ABC):
    """
    Base class for specifications in the domain layer.
    
    A specification encapsulates a business rule or criteria that can be used for validation or selection.
    """
    
    @abstractmethod
    def is_satisfied_by(self, candidate) -> bool:
        """
        Determine if the candidate satisfies the specification.
        
        Args:
            candidate (Any): The candidate to evaluate.
        
        Returns:
            bool: True if the candidate satisfies the specification, False otherwise.
        """
        pass
