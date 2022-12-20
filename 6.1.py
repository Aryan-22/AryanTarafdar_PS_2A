def transpose(m): #by default anticlockwise
    l = []
    a ,b= len(m), len(m[0])
    for i in range(b):
        l.append([])
        for j in range(a):
            l[i].append(m[j][i])
    return l
def clockrotate90(m):
    for i in m:
        m[i] = list(reversed(m[i]))



print(clockrotate90([[1,2],[3,4]]))