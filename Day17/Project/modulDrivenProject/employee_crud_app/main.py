import mysql.connector

from database.connection import get_connection
from operations.create_employee import add_employee
from operations.read_employee import (
    count_employees,
    search_employee_by_id,
    search_employee_by_name,
    view_all_employees,
)
from operations.update_employee import update_employee
from operations.delete_employee import delete_all_employees, delete_employee


def display_menu():
    print("\n========== EMPLOYEE MANAGEMENT SYSTEM ==========")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee by ID")
    print("4. Search Employee by Name")
    print("5. Update Employee")
    print("6. Delete One Employee")
    print("7. Delete All Employees")
    print("8. Count Employees")
    print("9. Exit")
    print("================================================")


def main():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        print("Database connected successfully.")

        while True:
            display_menu()
            choice = input("Enter your choice (1-9): ").strip()

            if choice == "1":
                add_employee(cursor, connection)
            elif choice == "2":
                view_all_employees(cursor)
            elif choice == "3":
                search_employee_by_id(cursor)
            elif choice == "4":
                search_employee_by_name(cursor)
            elif choice == "5":
                update_employee(cursor, connection)
            elif choice == "6":
                delete_employee(cursor, connection)
            elif choice == "7":
                delete_all_employees(cursor, connection)
            elif choice == "8":
                count_employees(cursor)
            elif choice == "9":
                print("Thank you! Application closed.")
                break
            else:
                print("Invalid choice! Please select between 1 and 9.")

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
