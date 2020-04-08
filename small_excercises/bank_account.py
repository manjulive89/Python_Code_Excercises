#!/usr/bin/env python3

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: {self.balance}"

acc = Account(input(),input())
print(acc)
