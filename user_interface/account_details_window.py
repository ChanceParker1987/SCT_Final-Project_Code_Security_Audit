from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.

    Attributes:
        account (BankAccount): A copy of the provided account object for transactions.
        balance_updated (Signal): A signal emitted when the account balance is updated.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.

        Args:
            account: The bank account to be displayed.

        Returns:
            None
        """
        super().__init__()

        if isinstance(account, BankAccount):
            self.account = copy.copy(account)  

            self.account_number_label.setText(f"Account Number: {self.account.account_number}")
            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.__on_apply_transaction)
            self.withdraw_button.clicked.connect(self.__on_apply_transaction)
            self.exit_button.clicked.connect(self.__on_exit)
        else:
            QMessageBox.critical(self, "Invalid Account", "The provided account is not valid.")
            self.reject()

    def __on_apply_transaction(self):
        """
        Handles deposit and withdrawal transactions for the account.
        Updates the balance label on success or displays an error message on failure.

        Raises:
            ValueError: If the transaction amount is invalid or the operation fails.
        """
        try:
            amount = float(self.transaction_amount_edit.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Deposit Failed", "Please enter a valid numeric value for the transaction amount.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            transaction_type = None 

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)  
            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)  

            self.balance_label.setText(f"Balance: ${self.account.balance:,.2f}")

            self.balance_updated.emit(self.account)

            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.critical(self, "Transaction Failed", f"{transaction_type} failed: {str(e)}")
            self.transaction_amount_edit.clear()
            self.transaction_amount_edit.setFocus()
    
    def __on_exit(self):
        """
        Closes the Account Details dialog and returns the user to the Client Lookup Window.
        """
        self.close()
