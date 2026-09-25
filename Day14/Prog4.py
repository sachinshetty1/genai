data = {10, "Python", 5.5, True}
print(data)


numbers = {10, 20, 30, 40}
print(numbers)

students = {"Ravi", "Suma"}
students.add("Kiran");
print(students);

#update() – Add multiple values
students = {"Ravi", "Suma"}
students.update(["Kiran", "Anu"])
print(students)

#remove() – Remove a value
students = {"Ravi", "Suma", "Kiran"}
students.remove("Suma")
print(students)

#discard() – Safely remove a value
students = {"Ravi", "Suma"}
students.discard("Thanesh")
print(students)
