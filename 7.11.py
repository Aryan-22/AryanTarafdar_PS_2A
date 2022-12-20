def clean(l):
    n = ""
    for i in range(len(l)):
        if (i == 0 or i == len(l) - 1) and l[i] == " ":
            continue
        else:
            n += l[i]
    return n

n = input()
print(clean(n))
