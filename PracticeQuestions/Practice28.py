# create bank account with 2 attributes balance and account number
# create methods to debit , credit , and print the balance
class Account:
    def __init__(self,balance,accNo):
        self.balance = balance
        self.accountnumber = accNo

    def debit(self , amount):
        self.balance -= amount
        print("Rs." , amount , "was debited")
        print("total balance=" , self.get_balance())

    def credit(self , amount):
        self.balance += amount
        print("Rs." , amount , "was credited")
        print("total balance=" , self.get_balance())

    def get_balance(self):
        return self.balance

account1 = Account( 50000 , 12345)
print(account1)    
print(account1.balance)
print(account1.accountnumber)
account1.debit(1000)
account1.credit(400)