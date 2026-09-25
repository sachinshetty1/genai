fruits = ["Apple", "Mango", "Banana"]

print(fruits);
print(fruits[0])   # Apple
print(fruits[1])   # Mango
print(fruits[-1])  # Banana


fruits.append("Orange")       # Adds at the end
fruits.insert(1, "Grapes")    # Adds at index 1
print(fruits);

fruits[0] = "Watermelon"
print(fruits);
fruits.remove("Mango")  # Removes by value
print(fruits);

fruits.pop()            # Removes the last item
print(fruits);

fruits.pop(1)           # Removes item at index 1
print(fruits);

del fruits[0]           # Removes item at index 0
print(fruits);

fruits.clear()          # Removes all items
print(fruits);
for fruit in fruits:
    print(fruit);
    
if "Mango" in fruits:
    print("Mango is available")
    
    
numbers = [30, 10, 20, 10]

numbers.append(40)
numbers.insert(1, 50)
numbers.remove(10)
numbers.sort()
numbers.reverse()

print(numbers.count(10))
print(numbers.index(20))

