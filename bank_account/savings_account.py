"""
Description: Module 2 Assignment 2: SavingsAccount Class
Author: Chance Parker
"""
from datetime import date, timedelta
from client.client import Client
from bank_account.bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    """
    SavingsAccount class: Represents a specific bank account with a minimum balance.

    Attributes:
        __minimum_balance (float): The minimum balance required for the account.
        __service_charge_strategy (MinimumBalanceStrategy): Strategy for calculating service charges.

    Methods:
        get_service_charges: Calculates and returns the service charges based on whether
        the minimum balance is met or not. 
    """

    def __init__(self, account_number, client_number, balance, minimum_balance, date_created = None):
        super().__init__(account_number, client_number, balance, date_created)
        """
        Initializes the SavingsAccount object on received arguments
        (if valid). Inherits from the BankAccount class.

        Args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            minimum_balance (float): The minimum balance required for the account.
            date_created (date): The date the account was created, defaults to today. 

        Raises:
            ValueError if any of the arguments are invalid.
        """

        if isinstance(minimum_balance, (int, float)):
            self.__minimum_balance = float(minimum_balance)
        else:
            self.__minimum_balance = 50.00

        self.__service_charge_strategy = MinimumBalanceStrategy(self.__minimum_balance)

    def __str__(self) -> str:
        """
        Returns a string representation of the SavingsAccount instance.

        Returns: 
            str: The savings account instance as a formatted string.
        """ 
        account_info = super().__str__()  

        return (f"{account_info}\n"
                f"Minimum Balance: ${self.__minimum_balance:.2f}\n"
                f"Account Type: Savings")

    def get_service_charges(self) -> float:
        """
        Calculates the service charges based on the account balance.

        Returns: 
            float: The calculated service charge.
        """
        return self.__service_charge_strategy.calculate_service_charges(self)