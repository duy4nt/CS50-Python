class Account:
    def __init__(self):
        self.balance = 0

    @property
    def balance(self):
        return self.balance

    def deposit(self, n):
        self.balance += n

    def withdraw(self, n):
        self.balance -= n

    def main():
        account = Account()
        print(account.balance)
        account.deposit(100)
        account.withdraw(50)
        print(account.balance)