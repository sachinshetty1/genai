class Suresh:
    def parentDetails(self):
        print("Parent Name: Suresh")

class Sindu(Suresh):
    def childDetails(self):
        print("Child Name: Sindu")

class Bindu(Suresh):
    def childDetails(self):
        print("Child Name: Bindu")



# Sindu object
s = Sindu()
s.childDetails()
s.parentDetails()

print("=====================")

# Bindu object
b = Bindu()
b.childDetails()
b.parentDetails()