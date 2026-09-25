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
print("=========")
print("\nEmployee Name:")
print(employee["name"])
print("\nEmployee Skills:")
print(employee.get("skills"));
employee["city"] = "Bangalore";

print("\nAfter Adding City and Experience:")
print(employee)

employee["salary"] = 60000
print(employee)