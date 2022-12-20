x = input()
y = input()
d1 = {}
ans = []
for i in x:
    if i not in d1.keys():
        d1[i] = 1
    else:
        d1[i] += 1
for i in y:

    if i in  d1.keys():
        ans.append(i)
        d1[i] -= 1
        if d1[i] == 0:
            del d1[i]

print(ans)



