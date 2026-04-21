"""
Description: Module 3 Assignment 3: ManagementFeeStrategy
Author: Chance Parker
"""
from bank_account.bank_account import BankAccount
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy
from datetime import date, timedelta

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Strategy for calculating service charges on accounts with managements fees.

    Attributes:
        __date_created (date): The date the account was created.
        __management_fee (float): The fee for managing the account.

    Constant:
        TEN_YEARS_AGO (date): The date ten years ago from today.
    """
    
    TEN_YEARS_AGO = date.today() - timedelta(days = 10 * 365.25)

    def __init__(self, date_created: date, management_fee: float):
        """
        Initializes the ManagementFeeStrategy with the account creation date and management fee.

        Args:
            date_created (date): The date the account was created.
            management_fee (float): The fee charged for managing the account.
        """
        self.__date_created = date_created
        self.__management_fee = management_fee


    def calculate_service_charges(self, account: BankAccount)-> float:
        """
        Calculates the service charges based on the age of the account.

        Args:
            account (BankAccount): The bank account to calculate the charges for.

        Returns:
            float: The calculated service charge.
        """
        if self.__date_created < self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE
        else:
            return self.BASE_SERVICE_CHARGE + self.__management_fee
