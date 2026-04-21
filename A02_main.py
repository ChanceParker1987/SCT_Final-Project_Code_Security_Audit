"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
Author: ACE Faculty
Edited by: Chance Parker
Date: October 27, 2024
"""

# 1.  Import all BankAccount types using the bank_account package
from bank_account import *

#     Import date from datetime
from datetime import date

# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing_account = ChequingAccount(
    account_number=111111, 
    client_number=392475, 
    balance= -870.05, 
    date_created= date.today(), 
    overdraft_limit= -500.00, 
    overdraft_rate=0.02)

# 3. Print the ChequingAccount created in step 2.
print(chequing_account)

# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")

# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
chequing_account.deposit(1370.05)

# 4b. Print the ChequingAccount
print(chequing_account)

# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(f"Service Charges: ${chequing_account.get_service_charges():.2f}")


print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings_account = SavingsAccount(
    account_number=222222,
    client_number=392475,
    balance=500.00,
    minimum_balance=100.00,
    date_created=date.today())

# 6. Print the SavingsAccount created in step 5.
print(savings_account)

# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
savings_account.withdraw(450.00)
# 7b. Print the SavingsAccount.
print(savings_account)
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(f"Service Charges: ${savings_account.get_service_charges():.2f}")

print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
new_investment_account = InvestmentAccount(
    account_number=333333,
    client_number=392475,
    balance=10000.00,
    management_fee=2.55,
    date_created=date.today())

# 9a. Print the InvestmentAccount created in step 8.
print(new_investment_account)

# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(f"Service Charges: ${new_investment_account.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
old_investment_account = InvestmentAccount(
    account_number=444444,
    client_number=392475,
    balance=10000.00,
    management_fee=2.55,
    date_created=date(2012, 10, 27))

# 11a. Print the InvestmentAccount created in step 10.
print(old_investment_account)

# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(f"Service Charges: ${old_investment_account.get_service_charges():.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
chequing_service_charge = chequing_account.get_service_charges()
chequing_account.withdraw(chequing_service_charge)

savings_service_charge = savings_account.get_service_charges()
savings_account.withdraw(savings_service_charge)

new_investment_service_charge = new_investment_account.get_service_charges()
new_investment_account.withdraw(new_investment_service_charge)

old_investment_service_charge = old_investment_account.get_service_charges()
old_investment_account.withdraw(old_investment_service_charge)

# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing_account)
print(savings_account)
print(new_investment_account)
print(old_investment_account)

