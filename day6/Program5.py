class BankAccount:
    
    def createAccount(self, accNum, balance):
        print("Account created successfully!")
        print("Account Number:", accNum)
        print("Initial Balance:", balance)

        self.accNum = accNum
        self.balance = balance

    def deposit(self, depAmount):
        if depAmount > 0:
            self.balance = self.balance + depAmount
            print("Amount deposited successfully!")
            print("Deposited Amount:", depAmount)
        else:
            print("Deposit amount must be greater than zero.")
    # withdrawnAmount from ATM
    # withdrawnAmount from netbanking 
    # withdrawnAmount from cheq 
    def withdraw(self, withdrawnAmount):
        if withdrawnAmount <= 0:
            print("Withdrawal amount must be greater than zero.")

        elif withdrawnAmount <= self.balance:
            self.balance = self.balance - withdrawnAmount
            print("Withdrawal successful!")
            print("Withdrawn Amount:", withdrawnAmount)

        else:
            print("Insufficient balance!")
            print("Available Balance:", self.balance)

    def checkBalance(self):
        print("Account Number:", self.accNum)
        print("Current Balance: ₹", format(self.balance, ".2f"))


# Object creation
account1 = BankAccount()

print("Please enter the details to create your account")

accountNumber = input("Enter account number: ")
initialBalance = float(input("Enter initial balance: "))

account1.createAccount(accountNumber, initialBalance)

print("\n========== ACCOUNT DETAILS ==========")
account1.checkBalance()

print("\n========== DEPOSIT ==========")
depositAmount = float(input("How much do you want to deposit? "))
account1.deposit(depositAmount)
account1.checkBalance()

print("\n========== WITHDRAWAL ==========")
withdrawAmount = float(input("How much do you want to withdraw? "))
account1.withdraw(withdrawAmount)
account1.checkBalance()

print("\n========== FINAL BALANCE ==========")
account1.checkBalance()