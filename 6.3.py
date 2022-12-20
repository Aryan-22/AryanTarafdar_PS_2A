
def check(l):
    m = len(l)
    n = len(l[0])
    x = []
    y = []
    d1,d2 = 0, 0
    for i in range(m):
        x.append(sum(l[i]))
    for j in range(n):
        s = 0
        for i in range(m):
            s += l[j][i]
        y.append(s)
    s = 0
    for i in range(m):
        d1 += l[i][i]
        d2 += l[i][n - j - 1]
    if x == y and x[0] == d1 and d1 == d2:
        return 1
    return 0



print("enter the order of square matrix:\n")
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
print(check(l))






