"""
Description: Module 3 Assignment 3: ServiceChargeStrategy
Author: Chance Parker
"""
from bank_account.bank_account import BankAccount
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    """
    Abstract superclass for all service charge strategies.

    Constant:
        BASE_SERVICE_CHARGE (float): Base service for all accounts. 
    """

    BASE_SERVICE_CHARGE = 0.50

    @abstractmethod
    def calculate_service_charges(self, account: BankAccount)-> float:
        """
        Abstract method to calculate service charges for a bank account.

        Args:
            account (BankAccount): The bank account used to calculate service charges.

        Returns:
            float: The calculated service charge.
        """
        pass
