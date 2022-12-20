def p(n):
    for i in range(2,int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    return 1
x = int(input())
for i in range(1,x + 1):
        if i == 1:
            print(1,end = " ")
        else:
            for j in range(2,x + 1):
                if i % j == 0 and p(j):
                    print(j,end = " ")
                    break
