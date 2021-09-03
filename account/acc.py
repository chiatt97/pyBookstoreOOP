class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())
    
    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    """This class generates checking account objects""" #use instance.__doc__ to see this

    type="Checking"

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

checking = Checking("account\\balance.txt", 5)
checking.transfer(100)
checking.commit()
print(checking.balance)
#account=Account("account//balance.txt")
#print(account.balance)
#account.withdraw(20)
#account.deposit(10)
#print(account.balance)
#account.commit()