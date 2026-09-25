day = int(input("Enter a day number from 1 to 3: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 5:
            print("Friday")
    case _:
        print("Invalid day number")