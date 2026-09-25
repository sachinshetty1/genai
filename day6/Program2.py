class BankAccount :
    
    def createAccount(self):
        print("Create Account method called");
        
    def deposit(self) :
       print("Deposit method called");
       
    def withdraw(self) :
        print("Withdraw method called");
        
    def checkbalance(self):
       print("Check balance method called");
    
    
account1 = BankAccount(); # object creation
account1.createAccount();
account1.deposit();
account1.withdraw();
account1.checkbalance();