class Bank_management:
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposite(self,amount):
         self.balance += amount
         print("deposite amount:",amount)
    def withdraw(self,amount):
        if self.balance >= amount:
         self.balance -= amount
         print("withdraw amount:",amount)
        else:
            print("insufficient balance")
    def display_balance(self):
        print("account holder:",self.account_holder)
        print("counter",self.balance)
       
b1 = Bank_management("amit",10000)
b1.deposite(2000)
b1.withdraw(5000)
b1.display_balance()

