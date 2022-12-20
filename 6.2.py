def transpose(m): #by default anticlockwise
    l = []
    a ,b= len(m), len(m[0])
    for i in range(b):
        l.append([])
        for j in range(a):
            l[i].append(m[j][i])
    return l

def anticlockwise90(m):
    m =  list(reversed(transpose(m)))
    return m

print(anticlockwise90([[1,2],[3,4]]))