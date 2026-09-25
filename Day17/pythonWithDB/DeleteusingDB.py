import mysql.connector

connection = None
cursor = None

try:
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="MicroDegree"
    )

    cursor = connection.cursor(dictionary=True)
    print("Connection Done")

    employee_id = int(input("Enter employee ID to delete: "))

    # Fetch employee details
    select_sql = """
        SELECT id, name, age, salary, designation
        FROM employee
        WHERE id = %s
    """

    cursor.execute(select_sql, (employee_id,))
    employee = cursor.fetchone()

    if employee:

        print("\nEmployee Found")
        print("ID          :", employee["id"])
        print("Name        :", employee["name"])
        print("Age         :", employee["age"])
        print("Salary      :", employee["salary"])
        print("Designation :", employee["designation"])

        confirmation = input(
            "\nDo you really want to delete this employee? Yes/No: "
        ).strip()

        if confirmation.upper() == "YES":

            delete_sql = "DELETE FROM employee WHERE id = %s"
            cursor.execute(delete_sql, (employee_id,))
            connection.commit()

            print("Employee deleted successfully.")

        else:
            print("Delete cancelled.")

    else:
        print("Employee ID not found.")

# Handles invalid employee ID such as ABC
except ValueError:
    print("Invalid input! Employee ID must be a number.")

# Handles database-related errors
except mysql.connector.Error as error:

    if connection is not None and connection.is_connected():
        connection.rollback()

    print("Database error:", error)

# Always executes whether an exception occurs or not
finally:

    if cursor is not None:
        cursor.close()
        print("Cursor closed.")

    if connection is not None and connection.is_connected():
        connection.close()
        print("Database connection closed.")