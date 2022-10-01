bs = int(input())
grade = input()
allow = 0
if grade == "A":
    allow = 1700
elif grade == "B":
    allow = 1500
else:
    allow = 1300
totalSalary = 1.59 * bs + allow
print(int(totalSalary))