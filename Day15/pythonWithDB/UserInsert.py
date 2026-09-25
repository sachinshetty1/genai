import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="root",database="MicroDegree")
cursor = connection.cursor()
id = input("Enter employee ID: ").strip()
name = input("Enter employee name: ").strip()
age = input("Enter employee AGE: ").strip()
salary = input("Enter employee salary: ")
desig = input("Enter employee Designation: ").strip()
pan = input("Enter employee PAN: ").strip()

sql = """INSERT INTO employee (id,name,age,salary,designation,pan)VALUES (%s, %s, %s,%s,%s,%s)"""
values = (id,name, age, salary,desig,pan)
cursor.execute(sql, values)
connection.commit()
print("Employee inserted successfully")
cursor.close()
connection.close()