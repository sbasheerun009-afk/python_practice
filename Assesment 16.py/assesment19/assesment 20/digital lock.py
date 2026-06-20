class DigitalWallet:
    def __init__(self,username,password,balance):
        self.__balance = balance
        self.__password = password
        self.username = username
        self.Transactionhistory = 0
    def deposit(self,amount):
        self.__balance += amount
        self.Transactionhistory += 1

    def withdraw(self,amount,password):
        if self.__password == password:
            self.__balance -= amount
        elif amount > self.__balance:
            self.Transactionhistory += 1
            print("withdraw successfully")
        else:
            print("incorrect password")
    def Bankbalance(self,password):
        if self.__password == password:
            print("current_bankbalance:",self.__balance)
        else:
            print("incorrect password:")
    def history(self):
        print(self.Transactionhistory)
    def get_details(self):
        return self.__balance
username,password,Transactionhistory = input().split()
balance = int(input())   
D = DigitalWallet(username,password,Transactionhistory)
n = int(input())
for _ in range(n):
    
    

