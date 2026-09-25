import mysql.connector


# --------------------------------------------------
# Database connection
# --------------------------------------------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="MicroDegree"
    )


# --------------------------------------------------
# 1. Add Employee
# --------------------------------------------------
def add_employee(cursor, connection):
    try:
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").strip()
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        designation = input("Enter designation: ").strip()

        # Check whether ID already exists
        check_sql = "SELECT id FROM employee WHERE id = %s"
        cursor.execute(check_sql, (employee_id,))

        if cursor.fetchone():
            print("Employee ID already exists.")
            return

        insert_sql = """
            INSERT INTO employee
            (id, name, age, salary, designation)
            VALUES (%s, %s, %s, %s, %s)
        """

        employee_data = (
            employee_id,
            name,
            age,
            salary,
            designation
        )

        cursor.execute(insert_sql, employee_data)
        connection.commit()

        print("Employee added successfully.")

    except ValueError:
        print("Invalid input! ID, age and salary must be numbers.")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to add employee:", error)


# --------------------------------------------------
# 2. View All Employees
# --------------------------------------------------
def view_all_employees(cursor):
    try:
        sql = """
            SELECT id, name, age, salary, designation
            FROM employee
        """

        cursor.execute(sql)
        employees = cursor.fetchall()

        if employees:
            print("\nEmployee Details")
            print("-" * 85)
            print(
                f"{'ID':<10}"
                f"{'Name':<20}"
                f"{'Age':<10}"
                f"{'Salary':<15}"
                f"{'Designation':<20}"
            )
            print("-" * 85)

            for employee in employees:
                print(
                    f"{employee['id']:<10}"
                    f"{employee['name']:<20}"
                    f"{employee['age']:<10}"
                    f"{employee['salary']:<15}"
                    f"{employee['designation']:<20}"
                )

            print("-" * 85)

        else:
            print("No employees found.")

    except mysql.connector.Error as error:
        print("Unable to fetch employees:", error)


# --------------------------------------------------
# 3. Search Employee
# --------------------------------------------------
def search_employee(cursor):
    try:
        employee_id = int(input("Enter employee ID to search: "))

        sql = """
            SELECT id, name, age, salary, designation
            FROM employee
            WHERE id = %s
        """

        cursor.execute(sql, (employee_id,))
        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found")
            print("ID          :", employee["id"])
            print("Name        :", employee["name"])
            print("Age         :", employee["age"])
            print("Salary      :", employee["salary"])
            print("Designation :", employee["designation"])
        else:
            print("Employee ID not found.")

    except ValueError:
        print("Invalid input! Employee ID must be a number.")

    except mysql.connector.Error as error:
        print("Unable to search employee:", error)


# --------------------------------------------------
# 4. Update Employee
# --------------------------------------------------
def update_employee(cursor, connection):
    try:
        employee_id = int(input("Enter employee ID to update: "))

        select_sql = """
            SELECT id, name, age, salary, designation
            FROM employee
            WHERE id = %s
        """

        cursor.execute(select_sql, (employee_id,))
        employee = cursor.fetchone()

        if not employee:
            print("Employee ID not found.")
            return

        print("\nExisting Employee Details")
        print("ID          :", employee["id"])
        print("Name        :", employee["name"])
        print("Age         :", employee["age"])
        print("Salary      :", employee["salary"])
        print("Designation :", employee["designation"])

        print("\nEnter new employee details:")

        name = input("Enter new name: ").strip()
        age = int(input("Enter new age: "))
        salary = float(input("Enter new salary: "))
        designation = input("Enter new designation: ").strip()

        confirmation = input(
            "Do you really want to update this employee? Yes/No: "
        ).strip()

        if confirmation.upper() == "YES":
            update_sql = """
                UPDATE employee
                SET name = %s,
                    age = %s,
                    salary = %s,
                    designation = %s
                WHERE id = %s
            """

            updated_data = (
                name,
                age,
                salary,
                designation,
                employee_id
            )

            cursor.execute(update_sql, updated_data)
            connection.commit()

            print("Employee updated successfully.")
        else:
            print("Update cancelled.")

    except ValueError:
        print("Invalid input! ID, age and salary must be numbers.")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to update employee:", error)


# --------------------------------------------------
# 5. Delete Employee
# --------------------------------------------------
def delete_employee(cursor, connection):
    try:
        employee_id = int(input("Enter employee ID to delete: "))

        select_sql = """
            SELECT id, name, age, salary, designation
            FROM employee
            WHERE id = %s
        """

        cursor.execute(select_sql, (employee_id,))
        employee = cursor.fetchone()

        if not employee:
            print("Employee ID not found.")
            return

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

    except ValueError:
        print("Invalid input! Employee ID must be a number.")

    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to delete employee:", error)


# --------------------------------------------------
# Main menu
# --------------------------------------------------
connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)
    print("Database connected successfully.")
    while True:
        print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("================================================")
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            add_employee(cursor, connection)

        elif choice == "2":
            view_all_employees(cursor)

        elif choice == "3":
            search_employee(cursor)

        elif choice == "4":
            update_employee(cursor, connection)

        elif choice == "5":
            delete_employee(cursor, connection)

        elif choice == "6":
            print("Thank you! Application closed.")
            break
        else:
            print("Invalid choice! Please select between 1 and 6.")
except mysql.connector.Error as error:
    print("Database connection failed:", error)

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()

    print("Database connection closed.")