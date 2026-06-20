class Account:
    def __init__(self,account_no,holder_name,transaction_amount):
        self.account_no = account_no
        self.account_holder = holder_name
        self.transaction_amount = transaction_amount
    def detect_suspecious(self):
        for amount in self.transaction_amount:
            if amount > 100000:
                print(amount)
    def average_transaction(self):
        avg = sum(self.transaction_amount)/len(self.transaction_amount)
        return avg
    def negetive_balance(self):
        if sum(self.transaction_amount) < 0:
            print("negetive balance risk:")
acc = Account(2526101,"basheerun",[900,2000,-600])
acc.detect_suspecious()
print("Average Transaction:", acc.average_transaction())
acc.negetive_balance()






