# Custom exception class for balance errors (used when not enough money in account)
class BalanceException(Exception):
    pass

# Main class for a bank account
class BankAccount:
    # Constructor: sets up account with starting balance and name
    def __init__(self,initial_amount,acc_name):
        self.balance = initial_amount  # stores the account balance
        self.name = acc_name           # stores the account name
        print(f"\nAccount '{self.name}' created.\n")  # confirms account creation

    # Shows the current balance (called after deposit/withdraw)
    def get_balance(self):
        print(f"\n'{self.name}' Account Balance = ${self.balance:.2f}")  
    
    # Adds money to the account (deposit)
    def deposit(self,amount):
        self.balance = self.balance + amount  # increases balance
        print("Deposit Completed. \n") 
        self.get_balance()                    # shows updated balance

    # Checks if enough balance is available for withdrawal/transfer
    def viable_distraction(self,amount):
        if self.balance >= amount:
            return  # enough balance, so continue
        else:
            # Not enough balance, so raise custom exception
            raise BalanceException(f"Sorry, account '{self.name}' only has a balance ${self.balance:.2f}")
    
    # Removes money from the account (withdraw)
    def withdraw(self,amount):
        try:
            self.viable_distraction(amount)   # check balance first
            self.balance = self.balance - amount  # decrease balance
            print("Withdraw Completed.")
            self.get_balance()                # shows updated balance
        except BalanceException as error:
            print(f"\n Withdraw interuppted {error}")  # shows error if not enough balance
    
    # Transfers money from this account to another account
    def transfer(self, amount, account):
        try:
            print("******Beginning Transaction*****")
            self.viable_distraction(amount)   # check balance first
            self.withdraw(amount)             # withdraw from this account
            account.deposit(amount)           # deposit to another account
            print(f"Transfer Completed!!!!!!!!")
        except BalanceException as error:
            print(f"Transfer interuppted---XXX {error}")  # shows error if not enough balance

# Subclass for accounts that earn interest on deposits
class InterestRewardsAcc(BankAccount):
    # Adds money with 5% interest (overrides deposit method)
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)  # deposit + 5% interest
        print(f"Deposit {amount} Completed.")
        self.get_balance()                             # shows updated balance

# Subclass for savings accounts with a withdrawal fee
class SavingsAcct(InterestRewardsAcc):
    # Constructor: sets up account and sets withdrawal fee
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)  # call parent constructor
        self.fee = 5                                # fixed withdrawal fee

    # Removes money with a fee (overrides withdraw method)
    def withdraw(self,amount):
        try:
            self.viable_distraction(amount)         # check balance first
            self.balance = self.balance -(amount + self.fee)  # decrease balance with fee
            print(f"Withdraw {amount} Completed. \n")
            self.get_balance()                      # shows updated balance
        except BalanceException as error:
            print(f"\n Withdraw interuppted {error}")  # shows error if not enough balance