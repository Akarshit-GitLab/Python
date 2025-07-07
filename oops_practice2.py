# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance.

class Account:
    def __init__ (self,bal,acc):
        self.balance = bal
        self.account_no = acc



    # debit
    def debit(self,amount):
        self.balance -= amount
        print("this", amount ,"has been debited from your acc")
        print("this is your remaining balnce =",self.balance)

    # credit
    def credit(self,amount):
        self.balance += amount
        print("RS", amount ,"has been credited to your acc")
        print("total balnce =",self.balance)


acc1 = Account(10000,187473)
print("this is your account no : ", acc1.account_no)
acc1.debit(500)
acc1.credit(15000)