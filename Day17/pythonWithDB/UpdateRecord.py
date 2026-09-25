import mysql.connector
connection = mysql.connector.connect(host="localhost",user="root",password="root",database="MicroDegree")
cursor = connection.cursor()

sql = """INSERT INTO employee (id,name,age,salary,pan)VALUES (%s, %s, %s,%s,%s)"""
myemployee = (600,"Rajesh",30,70000,"ABC123");

cursor.execute(sql, myemployee)
connection.commit()
print("Employee inserted successfully");
cursor.close()
connection.close()