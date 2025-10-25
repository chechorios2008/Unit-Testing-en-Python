from datetime import datetime
from src.exceptions import InsufficientFundsError, WithdrawlTimeRestrictionError


class BanckAccount:
    """
    A class that represents a bank account and allows basic financial operations.

    Attributes:
        balance (float): The current balance of the account.

    Methods:
        deposit(amount): Adds funds to the account balance.
        withdraw(amount): Subtracts funds from the account balance.
        get_balance(): Returns the current balance.
    """
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('Cuenta creada')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._log_transaction(f"Deposited {amount}. New balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        now = datetime.now()
        if now.hour < 8 and now.hour > 17:
            raise WithdrawlTimeRestrictionError("En este horario no esta permitido esta trx.")
        if amount > 0:
            self.balance -= amount
            self._log_transaction(f"Withdrew {amount}. New balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Checked current balance: {self.balance}")
        return self.balance