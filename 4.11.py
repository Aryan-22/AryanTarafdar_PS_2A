def fib(n , p = 0, ne = 1):
    if n == 1:
        return p
    return fib(n - 1,ne,p + ne)
n = int(input())
print(fib(n))