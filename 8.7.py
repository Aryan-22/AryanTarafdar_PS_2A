def p(n):
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1
x = int(input())
for i in range(2,x + 1):
    if p(i) and x % i == 0:print(i,end = " ")
