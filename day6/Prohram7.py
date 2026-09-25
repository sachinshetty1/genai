class Employee:
    
    def createEmployee(self, employeeId, employeeName, salary):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.salary = salary

        print("Employee created successfully!")
        print("Employee ID:", self.employeeId)
        print("Employee Name:", self.employeeName)
        print("Initial Salary:", self.salary)

    def addBonus(self, bonusAmount):
        if bonusAmount > 0:
            self.salary = self.salary + bonusAmount
            print("Bonus added successfully!")
            print("Bonus Amount:", bonusAmount)
        else:
            print("Bonus amount must be greater than zero.")

    def deductSalary(self, deductionAmount):
        if deductionAmount <= 0:
            print("Deduction amount must be greater than zero.")

        elif deductionAmount <= self.salary:
            self.salary = self.salary - deductionAmount
            print("Salary deducted successfully!")
            print("Deducted Amount:", deductionAmount)

        else:
            print("Deduction cannot be greater than the salary.")
            print("Current Salary:", self.salary)

    def checkSalary(self):
        print("\n----- Employee Details -----")
        print("Employee ID:", self.employeeId)
        print("Employee Name:", self.employeeName)
        print("Current Salary:", self.salary)


# Object creation
employee1 = Employee()

# Taking employee details from the user
print("Please enter the employee details")

employeeId = int(input("Enter Employee ID: "))
employeeName = input("Enter Employee Name: ")
salary = float(input("Enter Initial Salary: "))

# Calling createEmployee()
employee1.createEmployee(employeeId, employeeName, salary)

# Adding bonus
bonusAmount = float(input("\nEnter Bonus Amount: "))
employee1.addBonus(bonusAmount)

# Deducting salary
deductionAmount = float(input("\nEnter Deduction Amount: "))
employee1.deductSalary(deductionAmount)

# Checking final salary
employee1.checkSalary()