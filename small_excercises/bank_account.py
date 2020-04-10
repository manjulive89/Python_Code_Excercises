#!/usr/bin/env python3

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = int(balance)
    
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount

        self.balance += deposit_amount

    def withdrawal(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        
        if self.balance - self.withdraw_amount >= 0:
            self.balance -= self.withdraw_amount
            print(f"Withdrawing: {withdraw_amount}")
        else:
            print(f"Not enough money on the account!")
        return f"Account balance: {self.balance}"

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

acc = Account(input("Account owner: "),input("Account amount: "))
acc.deposit(100)
acc.withdrawal(300)
print(acc)
