from typing import final
class Car :
    @final  
    def gare(self):
        print("5 Gare CAR ");

class BMW (Car): 
    pass ;

class Benz(Car):
    pass;    

class Toyato(Car):
    pass;

b = BMW();
b.gare();

bnz = Benz();
bnz.gare();

t=Toyato();
t.gare();