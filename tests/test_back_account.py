import unittest, os
from unittest.mock import patch
from src.banck_account import BanckAccount


class BanckAccountTest(unittest.TestCase):

    def setUp(self):
        self.account = BanckAccount(balance=100_000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def test_deposit(self):
        new_balance = self.account.deposit(450_000)
        ## assert new_balance == 550_000 
        self.assertEqual(new_balance, 550_000, "El balance no es igual.")

    def test_withdraw(self):
        new_balance = self.account.withdraw(80_000)
        self.assertEqual(new_balance, 20_000, "El balance no es igual.")

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 100_000, "El balance no es igual.")

    def test_transaction_log(self):
        self.account.deposit(200_000)
        #assert os.path.exists("transaction_log.txt")
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_count_transaccions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(50_000)
        assert self._count_lines(self.account.log_file) == 2