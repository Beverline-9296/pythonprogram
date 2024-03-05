#A python program to calculate the payroll
#create a class Employee
class Employee:
    def __init__(self, emp_id, name):
        self.name = name
        self.emp_id = emp_id

    def calculate_payroll(self):
        raise NotImplementedError

class SalaryEmployee(Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

class PayrollCalculator:
    def __init__(self):
        pass

    def calculate_salary(self):
        # Prompt the user to enter employee details
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        weekly_salary = float(input("Enter weekly salary: "))

        # Create an instance of SalaryEmployee with the provided information
        employee = SalaryEmployee(emp_id, name, weekly_salary)

        # Calculate weekly and monthly salary
        weekly_salary = employee.calculate_payroll()
        monthly_salary = weekly_salary * 4  # Assuming 4 weeks in a month

        # Display the results
        print("Weekly salary:", weekly_salary)
        print("Monthly salary:", monthly_salary)

# Create an instance of PayrollCalculator and call the calculate_salary method
#create object call emp
emp = PayrollCalculator()
emp.calculate_salary()
