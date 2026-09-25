import mysql.connector


def add_employee(cursor, connection):
    try:
        employee_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ").strip()
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        designation = input("Enter employee designation: ").strip()

        cursor.execute("SELECT id FROM employee WHERE id = %s", (employee_id,))
        if cursor.fetchone():
            print("Employee ID already exists.")
            return

        sql = """
            INSERT INTO employee (id, name, age, salary, designation)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (employee_id, name, age, salary, designation))
        connection.commit()
        print("Employee added successfully.")

    except ValueError:
        print("Invalid input! ID, age and salary must be numbers.")
    except mysql.connector.Error as error:
        connection.rollback()
        print("Unable to add employee:", error)
