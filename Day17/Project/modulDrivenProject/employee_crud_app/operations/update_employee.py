import mysql.connector
from operations.read_employee import print_employee


def update_employee(cursor, connection):
    try:
        employee_id = int(input("Enter employee ID to update: "))
        cursor.execute(
            "SELECT id, name, age, salary, designation FROM employee WHERE id = %s",
            (employee_id,)
        )
        employee = cursor.fetchone()

        if not employee:
            print("Employee ID not found.")
            return

        print("\nCurrent Employee Details")
        print_employee(employee)
        print("\nPress Enter to keep the existing value.")

        name = input(f"New name [{employee['name']}]: ").strip() or employee["name"]
        age_text = input(f"New age [{employee['age']}]: ").strip()
        salary_text = input(f"New salary [{employee['salary']}]: ").strip()
        designation = (
            input(f"New designation [{employee['designation']}]: ").strip()
            or employee["designation"]
        )

        age = int(age_text) if age_text else employee["age"]
        salary = float(salary_text) if salary_text else employee["salary"]

        confirmation = input("Confirm update? Yes/No: ").strip().upper()
        if confirmation != "YES":
            print("Update cancelled.")
            return

        sql = """
            UPDATE employee
            SET name = %s, age = %s, salary = %s, designation = %s
            WHERE id = %s
        """
        cursor.execute(sql, (name, age, salary, designation, employee_id))
        connection.commit()
        print("Employee updated successfully.")

    except ValueError:
        print("Age and salary must be valid numbers.")
    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to update employee:", error)
