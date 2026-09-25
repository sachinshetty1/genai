class Vechical :    
    def move(self):
        print("Vechical moves")
    def fule(self):
        print("Vechical uses fule")
class Car(Vechical):
    def move(self):
         print("Car moves on the road")
class Boat(Vechical)    :
    def move(self):
        print("Boat moves on water")
class Aeroplane(Vechical):
    def move(self):
        print("Aeroplane flies in the sky")
car = Car()
car.move()          #Car moves on the road
car.fule()          #Vechical uses fule

boat = Boat()
boat.move()        #Boat moves on water
boat.fule()        #Vechical uses fule

aeroplane = Aeroplane()
aeroplane.move()    #Aeroplane flies in the sky
aeroplane.fule()    #Vechical uses fule