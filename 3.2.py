def fact(n):
    if n == 1:
        return 1
    res = n * fact(n - 1)
    return res
s = 0
n = int(input())
for i in range(1,n + 1):
    s += i / fact(i)
print(s)