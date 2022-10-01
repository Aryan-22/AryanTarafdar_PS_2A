def numberPattern(N):
    l = []
    for i in range(N):
        k = []
        for j in range(2 * i + 1):
            if j < i + 1:
                k.append((j + 1))
            else:
                k.append((k[-1] - 1))
        a = [str(i) for i in k]
        c = "".join(a)
        l.append(c)

    return " ".join(l)
n = int(input())
print(numberPattern(n))