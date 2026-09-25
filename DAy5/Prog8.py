while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Check Even or Odd")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Answer:", a + b)
        case 2:
            number = int(input("Enter a number: "))
            if number % 2 == 0:
                print("Even number")
            else:
                print("Odd number")
        case 3:
            print("Program closed")
            break
        case _:
            print("Invalid choice")
            continue
