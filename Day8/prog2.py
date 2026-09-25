class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
     animal.sound()
print("================");
# Creating separate objects
dog = Dog()
cat = Cat()
cow = Cow()
# Calling methods
dog.sound()
cat.sound()
cow.sound()