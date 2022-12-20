def transpose(m):
    l = []
    a ,b= len(m), len(m[0])
    for i in range(b):
        l.append([])
        for j in range(a):
            l[i].append(m[j][i])
    return l
def anticlockwise90(m):
    if m == []:
        return []
    m =  list(reversed(transpose(m)))
    return m
def solve(m):
    if m == []:
        return []
    return m[0] + solve(anticlockwise90(m[1:]))
print("enter rows of your matrix\n")
a = int(input())
l = []

print("enter your matrix:\n")
for i in range(a):
    x = input().split()
    l.append(x)
print(solve(l))
