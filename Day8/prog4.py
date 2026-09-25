def commonFunction():
    print("This is a common function for all the classes")
    
class Car :    
    def move(self):
        print("Car moves on the road")
    
car = Car()
car.move()          #Car moves on the road

commonFunction();