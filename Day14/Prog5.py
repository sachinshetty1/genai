students = set()
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Delete All Students")
    print("7. Exit")
    choice = input("Enter your choice: ").strip()
    # CREATE
    if choice == "1":
        name = input("Enter student name: ").strip()
        if name == "":
            print("Student name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            students.add(name)
            print("Student added successfully.")
    # READ
    elif choice == "2":
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nStudent List:")
            for number, student in enumerate(
                sorted(students), start=1
            ):
                print(number, student)
    # SEARCH
    elif choice == "3":
        name = input("Enter student name to search: ").strip()
        if name in students:
            print(name, "is available.")
        else:
            print("Student not found.")

    # UPDATE
    elif choice == "4":
        old_name = input("Enter existing student name: ").strip()

        if old_name not in students:
            print("Student not found.")

        else:
            new_name = input("Enter new student name: ").strip()

            if new_name == "":
                print("New student name cannot be empty.")

            elif new_name in students:
                print("New student name already exists.")

            else:
                students.remove(old_name)
                students.add(new_name)
                print("Student updated successfully.")

    # DELETE ONE
    elif choice == "5":
        name = input("Enter student name to delete: ").strip()

        if name in students:
            students.remove(name)
            print("Student deleted successfully.")

        else:
            print("Student not found.")

    # DELETE ALL
    elif choice == "6":
        if len(students) == 0:
            print("No students available to delete.")

        else:
            confirmation = input(
                "Are you sure you want to delete all students? "
                "(yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                students.clear()
                print("All students deleted successfully.")

            else:
                print("Delete operation cancelled.")

    # EXIT
    elif choice == "7":
        print("Thank you for using the application.")
        break

    else:
        print("Invalid choice. Enter a number from 1 to 7.")

