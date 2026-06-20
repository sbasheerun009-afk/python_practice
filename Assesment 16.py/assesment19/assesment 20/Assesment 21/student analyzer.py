class Student:
    def __init__(self, name, marks):
        self.__name = name          
        self.__marks = marks        
    def get_name(self):
        return self.__name
    
    def get_marks(self):
        return self.__marks

class ResultAnalyzer(Student):
    def get_average(self):
        marks = self.get_marks()
        if len(marks) == 0:
            return 0
        return sum(marks) / len(marks)
    
    def get_highest(self):
        return max(self.get_marks())
    
    def count_passed_subjects(self):
        count = 0
        for m in self.get_marks():
            if m >= 50:
                count += 1
        return count
    
    def reverse_name(self):
        return self.get_name()[::-1]

# Input
name = input()
n = int(input())
marks = list(map(int, input().split()))

# Object create
student = ResultAnalyzer(name, marks)

# Output
print(f"Name: {student.get_name()}")
print(f"Reversed Name: {student.reverse_name()}")
print(f"Average: {student.get_average()}")
print(f"Highest: {student.get_highest()}")
print(f"Passed Subjects: {student.count_passed_subjects()}")

        

