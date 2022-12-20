def lc(a,b):
    x, y = max(a, b), min(a, b)
    if (a == 1 or b == 1) or x % y != 0:
        return a * b
    if x % y == 0:
        return x

a = int(input())
b = int(input())
print(lc(a,b))