try :
    number1 = int(input("Enter A Number "));
    number2 = int(input("Enter A Number "));
    result = number1 / number2;
    print("The Result is: ", int(result));
    add_value = int(input("How much you want to add to the result  ? "))
    result = result + add_value;
    print("The Result after adding ", add_value, " is: ", int(result));
    print("===============")
    file = open("student.txt", "r")
    content = file.read()
    print(content)
    print("===============")
    students = ["Rahul", "Priya", "Anand"]
    print(students[5])
except ValueError:
    print("Please enter a valid integer.");
except ZeroDivisionError:
    print("Division by zero is not allowed."); 
except TypeError :
    print("Please enter a valid integer for addition.");
except FileNotFoundError:
    print("The file 'student.txt' was not found.");
except IndexError:
    print("The requested index does not exist.")
finally : 
    print("Execution completed.Thank you for using the program.");
    file.close();