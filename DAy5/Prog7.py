gender = input("Enter gender (Boy/Girl): ")
age = int(input("Enter age: "))
if (gender == "Boy" and age >= 21) or (gender == "Girl" and age >= 18):
    print("Eligible to vote")
else:
    print("Not eligible to vote")