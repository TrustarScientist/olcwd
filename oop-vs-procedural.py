"""
    procedural code implementation
"""
database = {
    "Dan": 300,
    "Ola": 56
}

def createAccount(username, initial_deposit=0):
    if username not in database:
        database[username] = initial_deposit


def withdraw(username, amount):
    if username in database:
        if database[username] >= amount:
            database[username] -= amount
        else:
            print("Insufficient funds")
    else:
        print("User not found")


def info(username):
    if username in database:
        print(f"{username}: ${database[username]}")
    else:
        print("User not found")







"""
    Object Oriented Code Implementation
"""

class Account:
    database = {
        "Dan": 300,
        "Ola": 56
    }

    def __init__(self, username, initial_deposit=0):
        self.username = username
        self.balance = initial_deposit
        Account.database[username] = initial_deposit

    
    def withdraw(self, amount):
        if self.username in Account.database:
            if Account.database[self.username] >= amount:
                Account.database[self.username] -= amount


    def info(self):
        if self.username in Account.database:
            print(f"{self.username}: ${Account.database[self.username]}")
        else:
            print("User not found")







    
        








