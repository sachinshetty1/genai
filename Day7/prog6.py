class Suresh: 
    # Parent class constructor
    def __init__(self):
        self.sites = 5
        self.money = 500000
        self.cars = 2
        self._brush=1;
       
class Sindu(Suresh):
    def childDetails(self):
        print("Child Name: Sindu") ;
        print("Number of Sites:", self.sites)
        print("Money: ₹", self.money)
        print("Number of Cars:", self.cars)
        print("Brush : " , self.brush)

class Bindu(Suresh):
    def childDetails(self):
        print("Child Name: Bindu")
        print("Number of Sites:", self.sites)
        print("Money: ₹", self.money)
        print("Number of Cars:", self.cars)
        print("Brush : " , self.brush)

# Sindu object
s = Sindu()
s.childDetails()
print("=====================")

# Bindu object
b = Bindu()
b.childDetails()
