

x = input().strip()
y = input().strip()
xl = [i for i in x]
yl = [i for i in y]
print(list(set(xl) ^ set(yl)))


