import math
def dsum(k):
    if k == 0:
        return 0
    r = k % 10
    return r + dsum(k // 10)
n = int(input())
if int(math.log10(n) + 1) % 2 == 1:
    x = int(math.log10(n)) + 1
    n1 = x // 2 + 1
    f1 = n // (10 ** (n1))
    f2 = n % (10 ** (n1 - 1))
    a,b= dsum(f1),dsum(f2)
    if a == b:
        print(1)
    else:
        print(0)


