from abc import ABC ,abstractmethod

class Parent(ABC):
    @abstractmethod
    def operation(self):
        pass
    @abstractmethod
    def utamadi(self):
       pass;
    @abstractmethod
    def myownothermethod(self):
        pass;

class Child(Parent):
    def operation(self):
        print("Abstract method is implemented in child class")
    def utamadi(self):
            print("Birinayni ")
    def myownothermethod(self):
            print("This is my own method in child class")

class Child2(Parent):
    def operation(self):
            print("Abstract method is implemented in child class")
    def utamadi(self):
            print("Veg birini ")
    def myownothermethod(self):
            print("This is my own method in child class")

c = Child();
c.operation()
c.utamadi();
c2 = Child2();
c2.operation()
c2.utamadi();