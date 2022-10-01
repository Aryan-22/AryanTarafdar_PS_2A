def consi(k):
    a = []
    n = len(k)
    s = 0
    for i in range(n):
        s = k[i]
        if i == n - 1:
            a.append(k[i])

        elif k[i] == k[i + 1]:
            continue
        elif k[i] != k[i + 1]:
            a.append(k[i])

    return a


def cons(k):
    c = 1
    a = []
    for i in range(len(k) - 1):
        if k[i] == k[i + 1]:
            c += 1
        else:
            a.append(str(c))
            c = 1
    a.append(str(c))
    return a
def lookandsay(target,n = 2,k = ["1","1"]):
    o = n
    if target == 1:
        return "1"
    if target == n:
        return "".join(k)
    l = []
    x = cons(k)
    y = consi(k)
    a , b = len(x),len(y)
    i , j = 0, 0
    while(i < a and j < b):
        l.append(x[i])
        l.append(y[j])
        i += 1
        j += 1
    o += 1
    return lookandsay(target,o,l)

n = int(input())
print(lookandsay(n))