x = input()
y = input()
xl =
d = {}
for i in x:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
for i in y:
    if i in d.keys():
        d[i] -= 1
        y.remove(i)
        if d[i] == 0:
            del d[i]
print(list(d.keys()) + y)

