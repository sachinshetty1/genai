class Bank :
    def roi(self):
        print("Rate of Interest is 8%");

class Sbi(Bank):
    def withdraw(self):
        print("SBI Withdraw Method");

class Icici(Bank):
    def roi(self):
        print("Rate of Interest is 9%");    # Method nameis same but implementation is different
        # over riding                       same method name but different bevihiour 
        
sbi = Sbi();
sbi.roi();              #8 %
sbi.withdraw();         #SBI Withdraw Method
icici = Icici();
icici.roi();            #9 %

print("=====================");
bank = Bank();
bank.roi();             #8 %