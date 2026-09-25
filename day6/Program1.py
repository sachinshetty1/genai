class Student : 
    def display(self):
        print("Welcome to Student Class ");
       
class Employee :
    def salary(self):
       pass;
        
    def display(self, message):
        print(message);

s = Student();      # object creation
s.display();

e = Employee(); 
e.display("Welcome to Employee Class ");
e.salary();
