n = int(input())
for i in range(n):
    for j in range(i):
        print(chr(65 + n - i + j),end = "")
    print()
