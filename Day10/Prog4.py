balance = 10000

try:
    maxtrylimit=5;
    while True:
        try:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                raise ValueError(
                    "Withdrawal amount must be greater than zero."
                )

            if amount > balance:
                raise Exception(
                    "Insufficient balance. Please enter a smaller amount."
                )

        except ValueError as userUnderstandableMsg:
            print("Invalid amount:", userUnderstandableMsg)
            print("Please try again.\n")

        except Exception as userUnderstandableMsg:
            print("Transaction failed:", userUnderstandableMsg)
            print("Available balance:", balance)
            print("Please try again.\n")

        else:
            balance = balance - amount

            print("Withdrawal successful!")
            print("Withdrawn amount:", amount)
            print("Remaining balance:", balance)

            break

finally:
    print("Your ATM card has been returned.")
    print("Thank you for using our ATM.")