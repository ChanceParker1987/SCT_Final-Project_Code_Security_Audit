"""
Description: Module 3 Assignment 3: MinimumBalanceStrategy
Author: Chance Parker
"""
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges based on a minimum balance requirement.

    Attributes:
        __minimum_balance (float): The required minimum balance for the account.

    Constant:
        SERVICE_CHARGE_PREMIUM (float): The premium multiplier applied if balance is below minimum.
    """
    
    SERVICE_CHARGE_PREMIUM = 2.0

    def __init__(self, minimum_balance: float):
        """
        Initializes the MinimumBalanceStrategy with the required minimum balance.

        Args:
            minimum_balance (float): The required minimum balance for the account.
        """
        self.__minimum_balance = minimum_balance

    def calculate_service_charges(self, account: BankAccount) -> float:
        """
        Calculates the service charges based on the account balance.

        Args:
            account (BankAccount): The bank account to calculate the charges for.

        Returns:
            float: The calculated service charge.
        """
        if account.balance > self.__minimum_balance:

            return self.BASE_SERVICE_CHARGE
        else:

            return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM


