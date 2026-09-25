import mysql.connector


def print_employee(employee):
    print("ID          :", employee["id"])
    print("Name        :", employee["name"])
    print("Age         :", employee["age"])
    print("Salary      :", employee["salary"])
    print("Designation :", employee["designation"])


def view_all_employees(cursor):
    try:
        cursor.execute(
            "SELECT id, name, age, salary, designation FROM employee ORDER BY id"
        )
        employees = cursor.fetchall()

        if not employees:
            print("No employees found.")
            return

        print("\n{:<8}{:<20}{:<8}{:<15}{:<20}".format(
            "ID", "Name", "Age", "Salary", "Designation"
        ))
        print("-" * 71)
        for employee in employees:
            print("{:<8}{:<20}{:<8}{:<15}{:<20}".format(
                employee["id"], employee["name"], employee["age"],
                employee["salary"], employee["designation"]
            ))
    except mysql.connector.Error as error:
        print("Unable to view employees:", error)


def search_employee_by_id(cursor):
    try:
        employee_id = int(input("Enter employee ID to search: "))
        cursor.execute(
            "SELECT id, name, age, salary, designation FROM employee WHERE id = %s",
            (employee_id,)
        )
        employee = cursor.fetchone()

        if employee:
            print("\nEmployee Found")
            print_employee(employee)
        else:
            print("Employee ID not found.")
    except ValueError:
        print("Employee ID must be a number.")
    except mysql.connector.Error as error:
        print("Unable to search employee:", error)


def search_employee_by_name(cursor):
    try:
        name = input("Enter employee name to search: ").strip()
        cursor.execute(
            """SELECT id, name, age, salary, designation FROM employee
               WHERE name LIKE %s ORDER BY name""",
            (f"%{name}%",)
        )
        employees = cursor.fetchall()

        if employees:
            for employee in employees:
                print("\nEmployee Found")
                print_employee(employee)
        else:
            print("No employee found with this name.")
    except mysql.connector.Error as error:
        print("Unable to search employee:", error)


def count_employees(cursor):
    try:
        cursor.execute("SELECT COUNT(*) AS total FROM employee")
        print("Total employees:", cursor.fetchone()["total"])
    except mysql.connector.Error as error:
        print("Unable to count employees:", error)
