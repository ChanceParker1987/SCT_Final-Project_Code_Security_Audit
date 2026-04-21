"""
Description: Module 3 Assignment 3: Subject Class
Author: Chance Parker
"""
from patterns.observer.observer import Observer

class Subject:
    """
    The Subject class is responsible for maintaining a list of its observers
    and notifying them of state changes or events.
    """

    def __init__(self):
        """
        Initializes the Subject with an empty list of observers.
        """
        self._observers = []

    def attach(self, observer: Observer) -> None:
        """
        Adds a new observer to the subject's list of observers.

        Args:
            observer (Observer): The observer to add.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """
        Removes an observer from the subject's list of observers.

        Args:
            observer (Observer): The observer to remove.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        """
        Alerts all registered observers of a state change.

        Args:
            message (str): The message to send to each observer.
        """
        for observer in self._observers:
            observer.update(message)
