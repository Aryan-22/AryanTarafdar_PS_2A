def fact(n):
    if n == 1 or n == 0:
        return 1
    res = n * fact(n - 1)
    return res
s = 0
n = 3
x = 1
for i in range(n):
    t = (-1) ** (i)
    s += (t) * (x ** (2 * i)) / fact(2 * i)
print(s)