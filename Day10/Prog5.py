balance = 10000
maxTryLimit = 5
attempt = 0
try:
    while attempt < maxTryLimit:
        try:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= 0:
                raise ValueError("Withdrawal amount must be greater than zero.")
            if amount > balance:
                raise Exception("Insufficient balance. Enter a smaller amount.")

        except ValueError as userUnderstandableMsg:
            attempt += 1
            print("Invalid amount:", userUnderstandableMsg)
            print("Attempt:", attempt, "of", maxTryLimit)
        except Exception as userUnderstandableMsg:
            attempt += 1
            print("Transaction failed:", userUnderstandableMsg)
            print("Available balance:", balance)
            print("Attempt:", attempt, "of", maxTryLimit)
        else:
            balance = balance - amount
            print("\nWithdrawal successful!")
            print("Withdrawn amount:", amount)
            print("Remaining balance:", balance)
            break
        if attempt < maxTryLimit:
            print("Please try again.\n")
    if attempt == maxTryLimit:
        print("\nMaximum attempt limit reached!")
        print("Your ATM card has been blocked.")    

finally:
    print("Your ATM card has been returned.")
    print("Thank you for using our ATM.")