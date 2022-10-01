def fact(n,c = 1):
    if n == 1 or n == 0:
        return c
    return fact(n - 1, c * n)
n = int(input())
print(fact(n))