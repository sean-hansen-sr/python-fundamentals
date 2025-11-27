from employee import SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for emp in self.employees:
            print(f"Employee: {emp.fname} {emp.lname}")
        print('--- End of Employee List ---')

    def pay_employees(self):
        print('Paying Employees:')
        for emp in self.employees:
            print(f"Paycheck for: {emp.fname} {emp.lname}")
            print(f"Amount: ${emp.calculate_paycheck():,.2f}")
            print('--- End of Paycheck ---')

def main():
    my_company = Company()

    employee1 = SalaryEmployee("John", "Doe", 52000)
    employee2 = HourlyEmployee("Jane", "Smith", 25, 50)
    employee3 = CommissionEmployee("Alice", "Johnson", 40000, 0.10, 5000)

    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()
