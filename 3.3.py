def fact(n):
    if n == 1 or n == 0:
        return 1
    res = n * fact(n - 1)
    return res
s = 0
n = int(input())
x = int(input())
for i in range(n):
    s += (x ** i) / fact(i)
print(s)