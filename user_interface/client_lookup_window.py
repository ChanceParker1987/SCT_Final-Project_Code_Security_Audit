from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot, Signal

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data, update_data
from bank_account import *

class ClientLookupWindow(LookupWindow):
    """
    A window for looking up and managing client accounts.

    Attributes:
        client_listing (dict): A dictionary of client data loaded from a file.
        accounts (dict): A dictionary of bank account data loaded from a file.
    """
    def __init__(self):
        """
        Initializes the ClientLookupWindow instance.
        Executes superclass initialization and sets up necessary attributes and event connections.

        Raises:
            Exception: If loading data from the files fails.
        """
        super().__init__()
        
        self.client_listing, self.accounts = load_data()
        
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.account_table.cellClicked.connect(self.on_select_account)
        self.client_number_edit.textChanged.connect(self.__on_text_changed)
        self.filter_button.clicked.connect(self.on_filter_clicked)
        
    @Slot()
    def __on_text_changed(self):
        self.account_table.setRowCount(0)

    def on_select_account(self, row: int, column: int):
        """
        Handles the event when a cell in the account_table is clicked.
        Opens an AccountDetailsWindow to display or edit the account details.

        Args:
            row (int): The row of the clicked cell in the account table.
            column (int): The column of the clicked cell in the account table.

        Raises:
            Exception: If an unexpected error occurs while opening the account details window.
        """
        try:
            account_number_item = self.account_table.item(row, 0)

            if not account_number_item or not account_number_item.text().strip():
                QMessageBox.warning(self, "Invalid Selection", "The selected account is invalid.")
                return

            account_number = int(account_number_item.text().strip())

            if account_number in self.accounts:
                selected_account = self.accounts[account_number]

                # Create the AccountDetailsWindow and connect the balance_updated signal
                account_details_window = AccountDetailsWindow(selected_account)
                account_details_window.balance_updated.connect(self.update_data)

                # Open the AccountDetailsWindow
                account_details_window.exec_()
            else:
                QMessageBox.warning(self, "Bank Account does not Exist", f"Account number {account_number} does not exist.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")

    def update_data(self, updated_account: BankAccount):
        """
        Updates the account table and the accounts.csv file with the updated balance.

        Args:
            updated_account (BankAccount): The updated BankAccount object.

        Raises:
            Exception: If updating the account data or file fails.
        """
        try:
            
            for row in range(self.account_table.rowCount()):
                account_number_item = self.account_table.item(row, 0)  

                if account_number_item and int(account_number_item.text()) == updated_account.account_number:
                    self.account_table.setItem(row, 1, QTableWidgetItem(f"${updated_account.balance:,.2f}"))
                    break

            self.accounts[updated_account.account_number] = updated_account

            update_data(updated_account)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update account: {str(e)}")

    def on_lookup_client(self):
        """
        Handles the lookup of a client based on the entered client number.
        Displays client details and their associated accounts in the account_table.
        
        Raises:
            ValueError: If the client number is invalid or not found.
        """
        try:
            client_number = int(self.client_number_edit.text().strip())
        except ValueError:
            QMessageBox.critical(self, "Non-Numeric Client", "Client Number must be a whole number.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.critical(self, "Client Not Found", f"Client Number {client_number} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_number]

        self.client_info_label.setText(f"Client Found: {client.first_name} {client.last_name}")

        self.account_table.setRowCount(0)

        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                account_number_item = QTableWidgetItem(str(account.account_number))
                account_number_item.setTextAlignment(Qt.AlignCenter)

                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight)

                date_created_item = QTableWidgetItem(str(account._date_created))
                date_created_item.setTextAlignment(Qt.AlignCenter)

                account_type_item = QTableWidgetItem(account.__class__.__name__)
                account_type_item.setTextAlignment(Qt.AlignCenter)

                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_created_item)
                self.account_table.setItem(row_position, 3, account_type_item)

        self.account_table.resizeColumnsToContents()

        self.toggle_filter(False)

    @Slot()
    def on_filter_clicked(self):
        """
        Handles the filtering of records in the account_table based on user-defined criteria.
        Toggles the display of the filtering widgets to indicate whether the table is filtered or complete.
        """
        filter_button_text = self.filter_button.text()

        if filter_button_text == "Apply Filter":

            filter_column_index = self.filter_combo_box.currentIndex()
            filter_text = self.filter_edit.text().strip()

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, filter_column_index)
                if item and filter_text.lower() in item.text().lower():
                    self.account_table.setRowHidden(row, False)  
                else:
                    self.account_table.setRowHidden(row, True)  

            self.filter_button.setText("Remove Filter")
            self.toggle_filter(True)  

        else:
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False) 

            self.filter_button.setText("Apply Filter")
            self.toggle_filter(False)  

    def toggle_filter(self, filter_on: bool):
        """
        Toggles the display and state of the filter widgets to indicate whether filtering is active.

        Args:
            filter_on (bool): Whether filtering is currently active.
        """
        self.filter_button.setEnabled(True)  

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")
