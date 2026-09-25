num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operator = input("Enter an operator (+, -, *, /): ")

# Validate the operator
while operator not in ("+", "-", "*", "/"):
    print("Invalid operator! Please enter only +, -, * or /.")
    operator = input("Enter an operator (+, -, *, /): ")

if operator == "+" :
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error: Cannot divide by zero")