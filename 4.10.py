def p(n,po):
    if po == 1:
        return n
    if po == 0 or n == 1:
        return 1
    if po % 2 == 0:
        return  p(n * n ,po / 2)
    if po % 2 != 0:
        return  n * p(n * n,(po - 1) / 2)
n = int(input())
po = int(input())
print(p(n,po))
