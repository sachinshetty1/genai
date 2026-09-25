number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
operator = input("Enter +, -, * or /: ")
match operator:
    case "+":
        result=number1 + number2;
        print("Result:", result)
    case "-":
        print("Result:", number1 - number2)
    case "*":
        print("Result:", number1 * number2)
    case "/":
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")