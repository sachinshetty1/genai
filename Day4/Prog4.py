class Student:
    def set_details(self):
        self.name = "Rahul"
        self.age = 21

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student()
student1.set_details()
student1.display_details()

