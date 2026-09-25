students = []

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

    # 1. Add student
    if choice == "1":
        name = input( "Enter student name (exactly 8 letters): ").strip()
        if name == "":print("Invalid name! Name cannot be empty ""or contain only spaces.")
        elif len(name) != 8: print( "Invalid name! Student name must contain ""exactly 8 characters.")
        elif not name.isalpha(): print("Invalid name! Student name must contain ""only letters." )
       
        else:
            students.append(name)
            print("Student added successfully!")

    # 2. View all students
    elif choice == "2":
        if len(students) == 0:
            print("No students available.")

        else:
            print("\n===== Student List =====")

            for number, student in enumerate(students, start=1):
                print(number, student)

    # 3. Search student
    elif choice == "3":
        name = input(
            "Enter student name to search: "
        ).strip()

        if name == "":
            print("Search name cannot be empty.")

        else:
            found_student = None

            for student in students:
                if student.casefold() == name.casefold():
                    found_student = student
                    break

            if found_student is not None:
                print("Student found:", found_student)

            else:
                print("Student not found.")

    # 4. Update student
    elif choice == "4":
        old_name = input(
            "Enter the student name to update: "
        ).strip()

        if old_name == "":
            print("Student name cannot be empty.")

        else:
            found_index = -1

            for index, student in enumerate(students):
                if student.casefold() == old_name.casefold():
                    found_index = index
                    break

            if found_index != -1:
                new_name = input(
                    "Enter new name (exactly 8 letters): "
                ).strip()

                if new_name == "":
                    print(
                        "Invalid name! New name cannot be empty "
                        "or contain only spaces."
                    )

                elif len(new_name) != 8:
                    print(
                        "Invalid name! New name must contain "
                        "exactly 8 characters."
                    )

                elif not new_name.isalpha():
                    print(
                        "Invalid name! New name must contain "
                        "only letters."
                    )

                elif any(
                    student.casefold() == new_name.casefold()
                    for index, student in enumerate(students)
                    if index != found_index
                ):
                    print("Another student already has this name.")

                else:
                    students[found_index] = new_name
                    print("Student updated successfully!")

            else:
                print("Student not found.")

    # 5. Delete student
    elif choice == "5":
        name = input(
            "Enter the student name to delete: "
        ).strip()

        if name == "":
            print("Student name cannot be empty.")

        else:
            found_index = -1

            for index, student in enumerate(students):
                if student.casefold() == name.casefold():
                    found_index = index
                    break

            if found_index != -1:
                deleted_student = students.pop(found_index)

                print(
                    deleted_student,
                    "deleted successfully!"
                )

            else:
                print("Student not found.")

    # 6. Delete all students
    elif choice == "6":
        if len(students) == 0:
            print("No student records are available to delete.")

        else:
            confirmation = input(
                "Do you really want to delete all records? "
                "(yes/no): "
            ).strip().casefold()

            if confirmation in ("yes", "y"):
                students.clear()
                print("All students deleted successfully!")

            else:
                print("No records were deleted.")

    # 7. Exit
    elif choice == "7":
        print("Thank you for using the application!")
        break

    # Invalid menu option
    else:
        print(
            "Invalid choice. Please enter a number from 1 to 7."
        )