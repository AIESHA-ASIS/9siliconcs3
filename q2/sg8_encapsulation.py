class BankAccount:
  def __init__(self, account_number, balance):
    self.set_account_number(account_number)
    self.set_balance(balance)

  def set_account_number(self, account_number):
    self.__account_number = account_number

  def set_balance(self, balance):
    if balance < 1:
      print("\nThe balance must not be a negative number")
      print(f"Account number: {self.__account_number}")
      Balance = abs(balance)
      print(f"Balance: {Balance}")
    else: 
      self.__balance = balance
      
  @property
  def get_account_number(self):
    return self.__account_number

  @property
  def get_balance(self):
    return self.___balance

def main():
  print("Account 1")
  account_number = int(input("Account number: "))
  balance = float(input("Balance: "))
  a1 = BankAccount(account_number, balance)
  print(a1)

main()
  