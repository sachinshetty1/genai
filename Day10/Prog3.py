try:
    balance = 10000
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        raise ValueError(" we cant withdraw Zero Rupees ")
    if amount > balance:
        raise Exception("Insufficient balance.")
    balance = balance - amount

except ValueError as userundrestandablemsg:
    print("Invalid amount:", userundrestandablemsg)
    
except Exception as userundrestandablemsg:
    print("Transaction failed:", userundrestandablemsg)
    
else:
    print("Withdrawal successful!")
    print("Remaining balance:", balance)
finally:
    print("Your ATM card has been returned.")
    print("Thank you for using our ATM.")