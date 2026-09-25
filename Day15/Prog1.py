class Employee :
        def createEmployee(self):
            self.id =input("ID : ");
            self.name= input("NAME :");
            self.age = input("Age : ");
            self.salary = input("Salary :")
            self.desig = input("Designation : ")

        def display(self):
            print("My iD is  : " , self.id ) ; 
            print("My Name  is  : " , self.name ) ; 
            print("My Age is  : " , self.age) ; 
            print("My Salary is  : " , self.salary ) ; 
            print("My Designation is  : " , self.desig ) ; 

emp = Employee();
emp.createEmployee();
emp.display();