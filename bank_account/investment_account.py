"""
Description: Module 2 Assignment 2: InvestmentAccount Class
Author: Chance Parker
"""
from datetime import date, timedelta
from client.client import Client
from bank_account.bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy 

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount class: Represents a specific bank account with a 
    management fee.

    Attributes:
        __management_fee (float): The fee for managing the investment account.
        __service_charge_strategy (ManagementFeeStrategy): Strategy for calculating service charges.
        
    Methods:
        get_service_charges: calculates and returns the service charges 
        based on the age of the account.
    """

    def __init__(self, account_number, client_number, balance, management_fee, 
                 date_created = None):
        super().__init__(account_number, client_number, balance, 
                         date_created)
        """
        Initializes the InvestmentAccount object on recieved arguments
        (if valid). Inherits from the BankAccount class.

        Args:
            account_number (int): The account's unique id.
            client_number (int): The client's unique id.
            balance (float): The balance of the bank account.
            date_created (date): The date the account was created, defaults to today. 
            management_fee (float): The fee to manage the investment account.

        Raises:
            ValueError if any of the arguments are invalid.
        """

        if isinstance(management_fee, (int, float)):
            self.__management_fee = float(management_fee)
        else:
            self.__management_fee = 2.55

        self.__service_charge_strategy = ManagementFeeStrategy(self._date_created, management_fee)

    def __str__(self)-> str:
        """
        Returns a string representation of the InvestmentAccount instance.

        Returns: 
            str: The investment account instance as a formatted string.
        """ 
        account_info = super().__str__()

        if self._date_created < ManagementFeeStrategy.TEN_YEARS_AGO:
            management_fee_str = "Waived"
        else:
            management_fee_str = f"${self.__management_fee:.2f}"

        return (f"{account_info}\nDate Created: {self._date_created} "
                f"Management Fee: {management_fee_str} Account Type: Investment")
    
    def get_service_charges(self)-> float:
        """
        Calculates the service charges based on the age of the account.

        Returns: 
            float: The calculated service charge.
        """
        return self.__service_charge_strategy.calculate_service_charges(self)
    
        
               

