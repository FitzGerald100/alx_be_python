class BankAccount:
    """A simple bank account class to merge deposits, withdrawals, and balance display."""

    def __init__(self, initial_balance=0):
        """initialize the bank account with an optional initial balance (default is 0). """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposite amount must be positive.")
        
    def withdraw(self, amount):
        """Withdraw the specified amount if sufficient funds are available.
        Returns True if successful, otherwise False."""
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                return True
            else:
                return False
        else:
            raise ValueError("Withdrawal amount must be positive.")
        
    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance:.2f}")