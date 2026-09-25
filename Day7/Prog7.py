class Father: 
    def money(self):
        print("Money")
    # Private method
    def __bpsuger(self):
        print("BP - Sugar")
   
class Mother:
    def care(self):
        print("Care")
class Child(Father, Mother):
    pass

print("=====================")
# Child object
c = Child()
c.money()
c.care()
# Private method cannot be called by the child
c.__bpsuger()