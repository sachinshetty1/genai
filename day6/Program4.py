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
        print("Current Balance:", self.balance)


# Object creation
account1 = BankAccount()

print("Please enter the details to create your account")

accountNumber = input("Enter account number: ")
initialBalance = int(input("Enter initial balance: "))

account1.createAccount(accountNumber, initialBalance)

print("\n========== ACCOUNT DETAILS ==========")
account1.checkBalance()

print("\n========== DEPOSIT ==========")
depositAmount = int(input("How much do you want to deposit? "))
account1.deposit(depositAmount)
account1.checkBalance()

print("\n========== WITHDRAWAL ==========")
withdrawAmount = int(input("How much do you want to withdraw? "))
account1.withdraw(withdrawAmount)
account1.checkBalance()

print("\n========== FINAL BALANCE ==========")
account1.checkBalance()