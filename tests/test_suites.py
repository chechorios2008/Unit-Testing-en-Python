import unittest
from test_back_account import BanckAccount


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BanckAccount("test_deposit"))
    suite.addTest(BanckAccount("test_withdraw"))
