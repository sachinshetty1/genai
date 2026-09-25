class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
    
    def Myname(self):
            print("Name:", self.name)
           
student1 = Student("Rahul", 21, "Python")
student1.display_details()
student1.Myname()

