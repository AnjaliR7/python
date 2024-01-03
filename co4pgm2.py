class BankAccount:
  def __init__(self,account_number,account_holder_name,account_type,balance=0):
    self.account_number=account_number
    self.account_holder_name=account_holder_name
    self.account_type=account_type
    self.balance=balance
  def deposit(self,amount):
    if amount>0:
     self.balance+=amount
     print("successful deposit of",amount)
     print("new balance=",self.balance)
    else:
       print("invalid amount")
  def withdraw(self,amount):
       if 0<amount <self.balance:
         self.balance=self.balance-amount
       elif amount>self.balance:
         print("not possible to withdraw")
       else:
         print("invalid")
  def get_balance(self):
    print("current_balance=",self.balance)
account1=BankAccount("123","anjali","savings",1000)
d=int(input("enter the amount of deposit:"))
account1.deposit(d)
w=int(input("enter the amount to wthdraw"))
account1.withdraw(w)
print(account1.get_balance())          
