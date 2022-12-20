import math

def arm(n,p):
    y = n
    s = 0
    while(y > 0):
        r = y % 10
        s += r ** p
        y = y // 10
    if s == n:
        return 1
    return 0

l = int(input())
u = int(input())
for i in range(l,u + 1):
    p = int(math.log10(i) + 1)
    if arm(i,p):
        print(i,end = " ")

