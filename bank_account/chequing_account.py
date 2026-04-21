"""
Description: Module 2 Assignment 2: ChequingAccount Class
Author: Chance Parker
"""
from datetime import date
from client.client import Client
from bank_account.bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy 

class ChequingAccount(BankAccount):
    """
    ChequingAccount class: Represents a specific type of bank account with 
    an overdraft.

    Attributes:
        __overdraft_limit (float): The overdraft limit of the account.
        __overdraft_rate (float): The interest rate applied to the overdraft amount.
        __service_charge_strategy (OverdraftStrategy): The strategy for calculating service charges.

    Methods:
        get_service_charges (float): calculates and returns the service charges 
        for the account based on the balance, overdraft_limit and overdraft_rate.
    """

    def __init__(self, account_number: int, client_number: int, 
                 balance: float, date_created: date = None, 
                 overdraft_limit: float = 0.0, overdraft_rate: float = 0.0):
        super().__init__(account_number, client_number, balance, date_created)
        """
        Initializes the ChequingAccount object on recievied arguments 
        (if valid). Inherits from the BankAccount class.

        Args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            date_created (date): The date the account was created, defaults to today.
            overdraft_limit (float): The overdraft limit of the chequing account.
            overdraf_rate (float): The interest rate of the overdraft.

        Raises:
            ValueError if any of the arguments are invalid.
        """

        if isinstance(overdraft_limit, (int, float)):
            self.__overdraft_limit = float(overdraft_limit)
        else:
            self.__overdraft_limit = -100.0

        if isinstance(overdraft_rate, (int, float)):
            self.__overdraft_rate = float(overdraft_rate)
        else:
            self.__overdraft_rate = 0.05

        self.__service_charge_strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)

    def get_service_charges(self) -> float:
        """
        Method to calculate service charges for the ChequingAccount.

        Returns: 
            float: The calculated service charges for the chequing account.
        """
        return self.__service_charge_strategy.calculate_service_charges(self)
    
    def __str__(self)-> str:
        """
        Returns a string representation of the ChequingAccount instance.

        Returns: 
            str: The ChequingAccount instance as a formatted string.
        """
        account_info = super().__str__()

        return (f"{account_info}\n"
                f"Overdraft Limit: {self.__overdraft_limit:.2f} Overdraft Rate: " 
                f"{self.__overdraft_rate * 100:.2f}% Account Type: Chequing")

