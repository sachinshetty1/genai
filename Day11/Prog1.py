from typing import final
class BankAccount:
    # if its private only same class can use 
    @final      #if it is final 
    def CreateAccount(self):
        print("Current Account");
        print("Saving Account");
        print("Student Account");
    def balance(self, amount):
        print("Balance  ", amount);
        
class SBI(BankAccount):
    def CreateAccount(self):
        print("Current Account");
        print("Saving Account");        # same method name and signatuire + diff implementation
    def OT(self, amount):
        print("SBI Balance  ", amount);
class ICICIC(BankAccount) : 
    def CreateAccount(self):
        print("Current Account");
        print("Saving Account");        # same method name and signatuire + diff implementation
bank = BankAccount();
bank.CreateAccount(); # private same class can use 
bank.balance(1000);
print("---------SBI --------------------");
sbi = SBI();    
sbi.CreateAccount();        # if its a private we can access in child 
                            #if its a final , we can access in child  / but we can not overrdide in child  
sbi.balance(2000);
sbi.OT(5000);
print("============= ICICIC=========")
i=ICICIC();
i.CreateAccount();