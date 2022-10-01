def calc(n):
    if n == 1:
        return 6
    s = (n) * (n + 1) * (n + 2) + calc(n - 1)
    return s
print(calc(2))