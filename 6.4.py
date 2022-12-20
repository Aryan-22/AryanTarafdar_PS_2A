print("enter the order of matrix:\n")
def transpose(m):
    l = []
    a ,b= len(m), len(m[0])
    for i in range(b):
        l.append([])
        for j in range(a):
            l[i].append(m[j][i])
    return l
def mirror(m): #reverses columns
    l = []
    for i in range(len(m)):
        l.append([])
        for j in range(len(m[0])):
            l[i].append(m[i][len(m[0]) - j - 1])
    return l
def clockrotate90(m):
    return mirror(transpose(m))
def deg180(m,n = 2):
    if n == 0:
        return m
    return deg180(clockrotate90(m),n - 1)
n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
print(deg180(l))