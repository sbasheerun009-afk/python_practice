'''class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def is_pass(self):
        return self.marks >= 40
    pass_count = 0
    try :
        with open("studenttext","r") as file:
            for line in file:
            try:
                name,marks= line.strip().split(",")
                marks = int(marks)
                S = Student(name,marks)
                if s.pass():
'''
'''class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def is_pass(self):
        return self.marks >= 40
passed_count = 0
try:
    with open("studenttxt", "w") as file:
        file.write("ravi,85\n")
        file.write("priya,42\n")
        file.write("kiran,abc\n")
        file.write("asha,91\n")
        file.seek(0)
    with open("studentext","r") as file:
        for line in file:
            print(line)
            try:
                name, marks = line.strip().split(",")
                marks = int(marks) 
                student = Student(name, marks)
                if student.is_pass():
                    passed_count += 1
            except ValueError:
                continue
            print(passed_count)
except FileNotFoundError:
    print("File Not Found")'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks >= 40


passed_count = 0

try:
    with open("students.txt", "w") as file:
        file.write("Ravi,85\n")
        file.write("Priya,42\n")
        file.write("Kiran,abc\n")
        file.write("Asha,91\n")
    with open("students.txt", "r") as file:
        for line in file:
            try:
                name, marks = line.strip().split(",")
                marks = int(marks)

                student = Student(name, marks)

                if student.is_pass():
                    passed_count += 1

            except ValueError:
                continue

    print(passed_count)

except FileNotFoundError:
    print("File Not Found")


