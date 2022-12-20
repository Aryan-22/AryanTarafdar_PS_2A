def comp(a,b):
    if len(a) == len(b) and  a == []:
        return True
    elif a[0] == b[0]:
        return comp(a[1:],b[1:])
    else:
        return False

a = input()
a = [i for i in a]
b = input()
b = [i for i in b]
print(comp(a,b))