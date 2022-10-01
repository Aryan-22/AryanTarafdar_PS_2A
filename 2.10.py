n = int(input())

for i in range(n):
    for j in range(2 * (n) - i - 1):
        if j < i  :
            print(end = " ")
        else:
            print("*",end = "")

    print()
for i in range(1,n):
    for j in range(n + i):
        if j < n - i - 1:
            print(end = " ")
        else:
            print("*",end = "")
    print()