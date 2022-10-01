x = float(input())
y = float(input())
if x >= 0 and y >= 0:
    print("1st")
elif x <= 0 and y <= 0:
    print("3rd")
elif x <= 0 and y >= 0:
    print("2nd")
else:
    print("4th")
