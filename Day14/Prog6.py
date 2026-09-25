# Employee Dictionary Program - Single File

employee = {
    "employee_id": 1001,
    "name": "Ramesh",
    "designation": "Developer",
    "salary": 50000,
    "skills": ["Java", "Spring Boot", "Angular"]
}

# 1. Display the complete dictionary
print("Employee Details:")
print(employee)

# 2. Read values
print("\nEmployee Name:")
print(employee["name"])

print("\nEmployee Skills:")
print(employee.get("skills"))

# 3. Add new data
employee["city"] = "Bangalore"
employee["experience"] = 5

print("\nAfter Adding City and Experience:")
print(employee)

# 4. Update existing data
employee["salary"] = 60000
employee["designation"] = "Senior Developer"

print("\nAfter Updating Salary and Designation:")
print(employee)

# 5. Delete data
employee.pop("experience")  # Deletes experience
del employee["city"]        # Deletes city

print("\nAfter Deleting Experience and City:")
print(employee)

# Safe deletion: no error if the key does not exist
employee.pop("course", None)

# 6. Display all keys
print("\nAll Keys:")
print(employee.keys())

# 7. Display all values
print("\nAll Values:")
print(employee.values())

# 8. Display all key-value pairs
print("\nAll Items:")
print(employee.items())

# 9. Iterate through the dictionary
print("\nEmployee Details Using Loop:")

for key, value in employee.items():
    print(key, ":", value)

# 10. Check whether a key exists
print("\nChecking Keys:")

if "salary" in employee:
    print("Salary is available:", employee["salary"])
else:
    print("Salary is not available")

# 11. Display the number of key-value pairs
print("\nNumber of Employee Properties:")
print(len(employee))

# 12. Copy the dictionary
employee_copy = employee.copy()

print("\nCopied Employee Dictionary:")
print(employee_copy)

# 13. Clear the copied dictionary
employee_copy.clear()

print("\nAfter Clearing the Copied Dictionary:")
print(employee_copy)

# 14. Display final employee dictionary
print("\nFinal Employee Dictionary:")
print(employee)


