def fact(n):
    if n == 1:
        return 1
    res = n * fact(n - 1)
    return res
n = int(input())
s = 0
for i in range(1,n + 1):
    s += fact(i)
print(s)
