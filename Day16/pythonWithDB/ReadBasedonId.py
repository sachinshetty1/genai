import mysql.connector
connection = mysql.connector.connect(host="localhost", user="root", password="root",database="MicroDegree")
cursor = connection.cursor(dictionary=True)
employee_id = int(input("Enter employee ID to search: "))
sql = "SELECT id, name, age, salary FROM employee WHERE id = %s";
print(sql);
cursor.execute(sql, (employee_id,))
employee = cursor.fetchone()
print(employee);
print("==================")
if employee:
    print("ID:", employee["id"])
    print("Name:", employee["name"])
    print("Age:", employee["age"])
    print("Salary:", employee["salary"])
else:
    print("Employee ID not found")
    cursor.close()
connection.close()