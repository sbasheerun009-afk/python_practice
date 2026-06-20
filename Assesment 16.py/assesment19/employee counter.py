class Employee():
    Employee_count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.Employee_count += 1
    def display_Employee(self):
        print("employee name:",self.name)
        print("employee salary:",self.salary)
    @classmethod
    def total_Employee(cls):
        print("total_Employee:",cls.Employee_count)
e1 = Employee("basheerun",15000)
e2 = Employee("basheera",2000)
e1.display_Employee()
e2.display_Employee()
e1.total_Employee()

