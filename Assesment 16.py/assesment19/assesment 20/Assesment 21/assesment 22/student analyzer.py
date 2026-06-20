class Student:
    def __init__(self,roll_num,name,attendence):
        self.roll_number = roll_num
        self.name = name
        self.attendence = attendence
    def attendence_percentage(self):

        total_days = len(self.attendence)
        present_count = self.attendence.count('p')
        percentage = (present_count/total_days)*100
        return self.percentage
    def below_75(self):
        self.attendence_percentage()
        if self.attendence_percentage() < 75:
            print("student:",self.roll_number,self.name)
    def longest_continues(self):
        self.longest_continues 

