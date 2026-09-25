class Student : 
    def __init__(self):
        print(" Student constructor  1  ");
    def __init__(self,name):
            print(" Student constructor  2  ");
    def display(self):
        print(" Student display method ");
    def accessCard(self):
            print(" Student Access card method  ");  

s = Student("Rahul");      # object creation
s.display();
s.accessCard();
s.display();
s.display();
s.display();
s.display();
s.display();
s.display();


s1 = Student("Rahul");      # object creation
s2 = Student("Rahul"); 
