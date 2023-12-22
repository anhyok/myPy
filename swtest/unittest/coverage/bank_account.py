# bank_account.py

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 양수여야 합니다.")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("잔액이 부족합니다.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
