class Animal : 
     def eat(self): 
            print("Will Eat")         
class Dog(Animal): 
    def sound(self):
        print("Dog barks ");
   
class Cat (Animal):  
    def sound(self):
        print("Meows ");
        
d = Dog();
d.sound();
d.eat();

print("=====================")
c = Cat();
c.eat();
c.sound();