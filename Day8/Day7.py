
class Car :    
    def move(self,maxlimit):
        for i in range(1, maxlimit):
                if i % 2 == 0:
                    print(i)

max_limit = int(input("Enter the number: "))
car = Car()
car.move(100)
