import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="root",database="MicroDegree")
cursor = connection.cursor(dictionary=True)
cursor.execute("SELECT id, name, age, salary , designation,pan FROM employee")
employees = cursor.fetchall()
print("=================================")
print(employees);
print("=================================")
if employees:
    print("\nEmployee Details")
    print("-" * 70)
    for emps in employees:
        print(emps["id"]," : ",emps["name"]," : ", emps["age"]);
else:
    print("No employees found")
cursor.close()
connection.close()