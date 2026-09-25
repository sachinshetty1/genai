import mysql.connector
from operations.read_employee import print_employee


def delete_employee(cursor, connection):
    """Delete one employee after fetching and displaying the record."""
    try:
        employee_id = int(input("Enter employee ID to delete: "))
        cursor.execute(
            "SELECT id, name, age, salary, designation FROM employee WHERE id = %s",
            (employee_id,)
        )
        employee = cursor.fetchone()

        if not employee:
            print("Employee ID not found.")
            return

        print("\nEmployee Found")
        print_employee(employee)

        confirmation = input("Delete this employee? Yes/No: ").strip().upper()
        if confirmation != "YES":
            print("Delete cancelled.")
            return

        cursor.execute("DELETE FROM employee WHERE id = %s", (employee_id,))
        connection.commit()
        print("Employee deleted successfully.")

    except ValueError:
        print("Employee ID must be a number.")
    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to delete employee:", error)


def delete_all_employees(cursor, connection):
    """Delete all employees after displaying the total and confirming twice."""
    try:
        cursor.execute("SELECT COUNT(*) AS total FROM employee")
        total = cursor.fetchone()["total"]

        if total == 0:
            print("No employees are available to delete.")
            return

        print("Total employees available:", total)
        confirmation = input(
            "Type DELETE ALL to remove every employee: "
        ).strip().upper()

        if confirmation != "DELETE ALL":
            print("Delete-all operation cancelled.")
            return

        cursor.execute("DELETE FROM employee")
        connection.commit()
        print(f"All {total} employees deleted successfully.")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to delete all employees:", error)
