class Bird:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def display(self):
        print("Bird Name:", self.name)
        print("Bird Color:", self.color)

# Objects of the Bird class
sparrow = Bird("Sparrow", "Brown")
pigeon = Bird("Pigeon", "Grey")
crow = Bird("Crow", "Black")
parrot = Bird("Parrot", "Green")

sparrow.display()
print()

pigeon.display()
print()

crow.display()
print()

parrot.display()