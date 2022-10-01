def fact(n):
    if n == 1 or n == 0:
        return 1
    res = n * fact(n - 1)
    return res
s = 0
n = int(input())
for i in range(1,n + 1):
    t = (-1) ** (i + 1)
    s += (i * t) / fact(2 * i - 1)
print(s)