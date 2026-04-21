import os
import sys
# THIS LINE IS NEEDED SO THAT THE GIVEN TESTING 
# CODE CAN RUN FROM THIS DIRECTORY.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import csv
from datetime import datetime
import logging
from bank_account import *
from client.client import Client

# *******************************************************************************
# GIVEN LOGGING AND FILE ACCESS CODE
 
# Absolute path to root of directory
root_dir = os.path.dirname(os.path.dirname(__file__))
 
# Path to the log directory relative to the root directory
log_dir = os.path.join(root_dir, 'logs')
 
# Create the log directory if it doesn't exist
os.makedirs(log_dir, exist_ok = True)
 
# Specify the path to the log file within the log directory
log_file_path = os.path.join(log_dir, 'manage_data.log')
 
# Configure logging to use the specified log file
logging.basicConfig(filename=log_file_path, filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s\n\n')
 
# Given File Path Code:
# Designed to locate the input files without providing any directory structure

# Construct the absolute path to the data directory at the root of the project
data_dir = os.path.join(root_dir, 'data')
 
# Construct the absolute paths to the data files
clients_csv_path = os.path.join(data_dir, 'clients.csv')
accounts_csv_path = os.path.join(data_dir, 'accounts.csv')
 
# END GIVEN LOGGING AND FILE ACCESS CODE
# *******************************************************************************


def load_data() -> tuple[dict, dict]:
    client_listing = {}
    accounts = {}

    # Load Clients
    with open(clients_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                client_number = int(record['client_number'])
                first_name = record['first_name'].strip()
                last_name = record['last_name'].strip()
                email_address = record['email_address'].strip()
                client = Client(client_number, first_name, last_name, email_address)
                client_listing[client_number] = client
            except Exception as e:
                logging.error(f"Error processing client record: {record}. Exception: {e}")

    # Load Accounts
    with open(accounts_csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for record in reader:
            try:
                account_type = record['account_type'].strip()
    
                account_number = int(record['account_number'])
                client_number = int(record['client_number'])
                balance = float(record['balance'])
                account_type = record['account_type'].strip()

                if account_type == "ChequingAccount":
                    account = ChequingAccount(account_number, client_number, balance)
                elif account_type == "SavingsAccount":
                    account = SavingsAccount(account_number, client_number, balance)
                elif account_type == "InvestmentAccount":
                    account = InvestmentAccount(account_number, client_number, balance)
                else:
                    logging.error(f"Invalid account type: {account_type} | Record: {record}")
                    continue

                if client_number in client_listing:
                    accounts[account_number] = account
                else:
                    logging.error(f"Bank Account {account_number} has invalid Client Number {client_number}")

            except ValueError as e:
                logging.error(f"Data parsing error in record {record}: {e}")
            except Exception as e:
                logging.error(f"Unexpected error processing record {record}: {e}")

    return client_listing, accounts

def update_data(updated_account: BankAccount) -> None:
    """
    A function to update the accounts.csv file with balance 
    data provided in the BankAccount argument.
    
    Args:
        updated_account (BankAccount): A bank account containing an updated balance.
    """
    updated_rows = []

    with open(accounts_csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        
        for row in reader:
            account_number = int(row['account_number'])
            if account_number == updated_account.account_number:
                row['balance'] = updated_account.balance
            updated_rows.append(row)

    with open(accounts_csv_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(updated_rows)

# GIVEN TESTING SECTION:
if __name__ == "__main__":
    clients,accounts = load_data()

    print("=========================================")
    for client in clients.values():
        print(client)
        print(f"{client.client_number} Accounts\n=============")
        for account in accounts.values():
            if account.client_number == client.client_number:
                print(f"{account}\n")
        print("=========================================")