import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="root",database="MicroDegree")
cursor = connection.cursor()
print("Connection DOne ")
employee_id = int(input("Enter employee ID to delete: "))       # 222 
confirmation = input("Dp you Really Want to Delete ?  Please Type Yes or NO .! "); #yes , YES , Yes , No NO no nO
if confirmation.upper()=="YES":
    sql = "DELETE FROM employee WHERE id = %s"; 
    cursor.execute(sql, (employee_id,));
    connection.commit()
    if cursor.rowcount > 0:
        print("Employee deleted successfully")
    else:
        print("Employee ID not found")
else :
    print("Delete Cancled...!!")



