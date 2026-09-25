students = []
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = input("Enter your choice: ")
    # Add student
    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print("Student added successfully!")
    # View all students
    elif choice == "2":
        if len(students) == 0:
            print("No students available.")
        else:
            print("\nStudent List:")

            for student in students:
                print(student)
    # Search student
    elif choice == "3":
        name = input("Enter student name to search: ")
        if name in students:
            print("Student found!")
        else:
            print("Student not found.")
    # Update student
    elif choice == "4":
        old_name = input("Enter the student name to update: ")
        if old_name in students:
            new_name = input("Enter the new name: ")
            index = students.index(old_name)
            students[index] = new_name
            print("Student updated successfully!")
        else:
            print("Student not found.")
    # Delete student
    elif choice == "5":
        name = input("Enter the student name to delete: ")
        if name in students:
            students.remove(name)
            print("Student deleted successfully!")
        else:
            print("Student not found.")
    # Exit
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")