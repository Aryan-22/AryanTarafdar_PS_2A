n = input()
d = {}
for i in n:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
print(d)