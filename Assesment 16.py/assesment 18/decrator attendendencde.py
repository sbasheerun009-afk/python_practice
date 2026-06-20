'''def student_attendece(func):
    def wrapper():
        print("students allowed")
        func()
        print("students not allowed" )
    return wrapper
@student_attendece
def display(name):
    print()'''
n = int(input())
for _ in range(n):
    name,percentage,medicaleave = input().split()
    percentage = int()
    medicaleave = int()
    if percentage >= 75 and medicaleave > 2:
        print(name,"allowed")
    else:
        print(name,"not allowed")
@