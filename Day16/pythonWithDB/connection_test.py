import mysql.connector
try:
    connection = mysql.connector.connect(host="localhost", user="root", password="root",database="MicroDegree");
    
    if connection.is_connected():
        print("Successfully connected to MySQL")

except mysql.connector.Error as error:
    print("Connection failed:", error)

finally:
    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("Connection closed")
