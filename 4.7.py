def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

def strong(n):
    y = n
    s = 0
    while(y > 0):
        r = y % 10
        s += fact(r)
        y = y // 10
    if s == n:
        return 1
    return 0

n = int(input())
for i in range(n + 1):
    if strong(i):
        print(i,end = " ")

