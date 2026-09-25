class BankAccount :
    def createAccount(self,accNum, balance):
        print("Create Account method called");
        print("Accout No is : " , accNum);
        print("Balalce is : " ,balance );
        self.accNum = accNum; # accNum to utilize globle  again re assignig using self 
        self.balance = balance;
    def deposit(self,depamount) :
        self.balance = self.balance + depamount;
        print("Amount Deposited ....!");
    def withdraw(self,withdrawnamount) :
        self.balance=self.balance-withdrawnamount;
        print("Withdraw Successfull...!");
    def checkbalance(self):
       print("My Account Balance is : " , self.balance );
account1 = BankAccount(); # object creation
print("We are Creating your account Please ENter ")
accno=input("Account No ");
bal = int(input("Inital balance "))
account1.createAccount(accno, bal);           # when i check the balace : 50000 
account1.checkbalance(); 
print("=====================");
depamount=int(input("How much you want to Depeosit "))#atm . bank , phone, netwo
account1.deposit(depamount);                         # after 5000 deposst : balalce : 55000
account1.checkbalance(); 
print("============================");
withdranamt=int(input("How much you want to WithDrawn "))
account1.withdraw(withdranamt);   
account1.checkbalance();                        #450000 
print("============================")
account1.checkbalance();                        # balance 45000