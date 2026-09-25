class Car:
    # Private method
    def __startCar(self):
        print("Car starting...")
        print("Checking engine...")
        print("Engine condition is good")
        print("Car started successfully!")

    # Public method
    def start(self):
        self.__startCar()


class BMW(Car) :
    def __startCar(self):
            print("Car starting...")
            print("All going good ")
    def abc(self):
        self.__startCar();
        print("Hi bmw ")

car = Car()
car.start()

print("===================")
bmw = BMW();                # child class can not access parent private methods 
#bmw.__startCar();
bmw.abc();