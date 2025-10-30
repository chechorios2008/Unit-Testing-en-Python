import unittest, os
from faker import Faker
from src.user import User
from src.banck_account import BanckAccount


class UserTests(unittest.TestCase):

    def setUp(self) -> None:
        self.faker = Faker(locale="es")
        self.user = User(name=self.faker.name(), email=self.faker.email())

    def test_user_creation(self):
        name_generate = self.faker.name()
        email_generate = self.faker.email()
        user = User(name=name_generate, email=email_generate)
        self.assertEqual(user.name, name_generate)
        self.assertEqual(user.email, email_generate)

    def test_user_with_multiple_accounts(self):
        user = User(name=self.faker.name(), email=self.faker.email())

        for _ in range(3):
            bank_account=BanckAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension=".txt")
            )
            self.user.add_account(account=BanckAccount)

        expected_value = self.user.get_total_balace()
        value = sum(account.get_balance() for account in self.accounts)
        self.assertEqual(value, expected_value)

    def tearDown(self) -> None:
        for account in self.user.accounts:
            os.remove(account.log_file)