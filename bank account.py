import random
print("BANK SYSTEM")
def create():
  print("for 1.new account\n 2.existing account")
  ch=int(input("enter choice:"))
  if ch==1:
    print("your account num is",random.randrange(5000,6000))
    User=input("enter user name:")
    password=input("ener password:")
    mobile=input("enter mobile num:")
    login()
  if ch==2:
    login()
def login():
  def accnum():
    account=input("enter account number:")
    if account.isdigit()==True:
      print(account)
    else:
      print("it is invaid\n,print again the account number")
      accnum()
  def name():
    User=input("enter user name:")
    if User is User:
      print(User)
    else:
      print("it is invaid\n,print again the account number")
      name()
  accnum()
  name()
create()
login()
password=input("access code:")
