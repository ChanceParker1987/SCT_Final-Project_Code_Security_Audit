"""
Description: Module 3 Assignment 3: Observer Class
Author: Chance Parker
"""
from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer superclass to define the interface for all concrete observers.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Update method to notify observers of changes.
        
        Args:
            message (str): The message containing information about the change.
        """
        pass


