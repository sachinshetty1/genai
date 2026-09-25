class BankAccount:
    def createAccount(self):
                self.accNo=input("Account No: ")
                self.name=input("Name: ")
                self.balance=float(input("Balance: "))
    def deposit(self):
                amt=float(input("Deposit: "))
                self.balance+=amt
    def withdraw(self):
                amt=float(input("Withdraw: "))
                if amt<=self.balance:
                    self.balance-=amt
                    print("Withdrawal Successful")
                else:
                    print("Insufficient Balance")
    def checkBalance(self):
                print("Account:",self.accNo)
                print("Name:",self.name)
                print("Balance:",self.balance)

class SavingsAccount(BankAccount):
    def interest(self):
        self.balance+=self.balance*0.05
        print("5% Interest Added")
        
class CurrentAccount(BankAccount):
    def interest(self):
        self.balance+=self.balance*0.05
        print("8% Interest Added")
sacc=SavingsAccount();
while True:
    print("\n1.Create Account")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Check Balance")
    print("5.Add Interest")
    print("6.Exit")
    choice=int(input("Enter Choice: "))
    if choice==1:
        sacc.createAccount()
    elif choice==2:
        sacc.deposit()
    elif choice==3:
        sacc.withdraw()
    elif choice==4:
        sacc.checkBalance()
    elif choice==5:
        sacc.interest()
    elif choice==6:
        break
    else:
        print("Invalid Choice")