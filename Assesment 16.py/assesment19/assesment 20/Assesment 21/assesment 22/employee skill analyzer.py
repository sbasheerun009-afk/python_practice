class Employee:
    def __init__(self, name, id, skill):
        self.employee_name = name
        self.employee_id = id
        self.employee_skill = list(set(skill))

n = int(input())

employees = []
all_skills = set() 
max_skills = 0
max_emp = None

for i in range(n):
    name = input()
    emp_id = int(input())
    skills = input().split(",")

    emp = Employee(name, emp_id, skills)
    employees.append(emp)

for emp in employees:

    all_skills.update(emp.employee_skill)

    if "python" in emp.employee_skill:
        print("Employee knowing Python:", emp.employee_name)

    if len(emp.employee_skill) > max_skills:
        max_skills = len(emp.employee_skill)
        max_emp = emp

print("Unique Skills:", len(all_skills))
print("Max Skills Employee:", max_emp.employee_name)

        