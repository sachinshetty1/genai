import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="MicroDegree"
)

cursor = connection.cursor(dictionary=True)

sql = """
SELECT id, name, age, salary, designation, pan
FROM employee
"""

cursor.execute(sql)

# Get column names from metadata
column_names = [column[0] for column in cursor.description]

# Fetch employee records
employees = cursor.fetchall()

print("\nEmployee Details")
print("-" * 90)

# Print column names
print(
    f"{column_names[0]:<10}"
    f"{column_names[1]:<20}"
    f"{column_names[2]:<10}"
    f"{column_names[3]:<15}"
    f"{column_names[4]:<20}"
    f"{column_names[5]:<15}"
)

print("-" * 90)

# Print values under column names
if employees:
    for employee in employees:
        print(
            f"{employee['id']:<10}"
            f"{employee['name']:<20}"
            f"{employee['age']:<10}"
            f"{employee['salary']:<15}"
            f"{employee['designation']:<20}"
            f"{employee['pan']:<15}"
        )
else:
    print("No employees found")

print("-" * 90)

cursor.close()
connection.close()