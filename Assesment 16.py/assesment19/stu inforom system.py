class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display_details(self):
        print("student details:")
        print("name:",self.name)
        print("roll_no:",self.roll_no)
        print("marks:",self.marks)
        if self.marks >= 35:
            print("pass")
        else:
            print("fail")
s1 = Student("basheerun","5e5",88)
print(s1.name)
print(s1.roll_no)
print(s1.marks)
s1.display_details()