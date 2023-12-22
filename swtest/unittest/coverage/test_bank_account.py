# test_bank_account.py

import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount()

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw(self):
        self.account.deposit(200)
        self.account.withdraw(100)
        self.assertEqual(self.account.get_balance(), 100)

    def test_withdraw_insufficient_balance(self):
        # with self.assertRaises(ValueError):
        #     self.account.deposit(-100)
        with self.assertRaises(ValueError):
            self.account.withdraw(100)

if __name__ == '__main__':
    unittest.main()
