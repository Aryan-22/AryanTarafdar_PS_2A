def g(a,b):
    if a[0] > b[0] :
        return "".join(a)
    elif a[0] < b[0]:
        return "".join(b)
    else:
        x = [a[0]] + g(a[1:],b[1:])
    return x
a = input()
b = input()
a = [i for i in a]
b = [i for i in b]
print(g(a,b))
