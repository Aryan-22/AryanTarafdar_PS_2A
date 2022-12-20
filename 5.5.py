n = int(input())
l = []
c = 0
for i in range(0,n):
    if i <= n // 2 and n & 1:
        l.append(2 * i + 1)
        c = i
    elif i < n // 2 and n & 1 == 0:
        l.append(2 * i + 1)
        c = i

    else:
        l.append(2 * (c + 1))
        c -= 1
print(l)


