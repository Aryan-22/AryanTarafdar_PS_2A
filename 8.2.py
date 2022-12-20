def p(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * p(a,b - 1)
def kth(a,k):
    return a[len(a) - k]
a,b,k = map(int,input().split())
x = list(str(p(a,b)))
print(kth(x,k))

