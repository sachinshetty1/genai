uname = input("Enter Name: ")
upass = input("Enter Password: ")
      #Suresh !="Thanesh"   and upass!="Thanesh@123"
while uname != "Thanesh" and upass != "Thanesh@123":
    print("Login Failed! Please try again.")
    uname = input("Enter Name: ")
    upass = input("Enter Password: ")

print("Login Successful!")
