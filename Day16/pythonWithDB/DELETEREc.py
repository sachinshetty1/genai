import mysql.connector
connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root",
 database="MicroDegree"
)
cursor = connection.cursor()
employee_id = int(input("Enter employee ID to delete: "))
confirmation = input("Type YES to confirm deletion: ")
if confirmation.upper() == "YES":
    sql = "DELETE FROM employee WHERE id = %s"
    cursor.execute(sql, (employee_id,))
    connection.commit()
    if cursor.rowcount > 0:
        print("Employee deleted successfully")
    else:
        print("Employee ID not found")
else:
 print("Deletion cancelled")
cursor.close()
connection.close()
