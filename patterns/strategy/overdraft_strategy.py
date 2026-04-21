"""
Description: Module 3 Assignment 3: OverdraftStrategy
Author: Chance Parker
"""
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges on accounts with an overdraft.
    
    Attributes:
        __overdraft_limit (float): The maximum overdraft allowed as a positive value.
        __overdraft_rate (float): The interest rate applied to the overdraft amount.
    """

    def __init__(self, overdraft_limit: float, overdraft_rate: float):
        """
        Initializes the OverdraftStrategy with attributes necessary for calculating
        service charges on overdraft accounts.

        Args:
            overdraft_limit (float): The maximum overdraft allowed.
            overdraft_rate (float): The interest rate for overdraft.
        """
        self.__overdraft_limit = overdraft_limit
        self.__overdraft_rate = overdraft_rate

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates service charges based on the overdraft rules.

        Args:
            account (BankAccount): The bank account to calculate the charges.
            
        Returns:
            float: The calculated service charge.
        """
        if account.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE
        else:
            overdraft_service_charge = ((self.__overdraft_limit - account.balance) 
                                        * self.__overdraft_rate)
            return self.BASE_SERVICE_CHARGE + overdraft_service_charge
