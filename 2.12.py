n = int(input())
for i in range(n):
    k = 1
    c = 0
    for j in range(2 * n - 1):
        if j < n - i:
            print(k,end = " ")
            k += 1
        elif c < 2 * i - 1:
            print(end = "  ")
            c += 1
        else:
            if i == 0 and j == n:
                k = n - c - 1
                print(k,end = " ")
                c += 1
            else:
                k -= 1
                print(k,end = " ")

    print()
