def prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

l = int(input())
u = int(input())
for i in range(l,u + 1):
    if prime(i):
        print(i,end = " ")
