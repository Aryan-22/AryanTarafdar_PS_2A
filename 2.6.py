n = int(input())
for i in range(n):
    k = i + 1
    for j in range(n + i):
        if j < n - i - 1:
            print(end = " ")
        else:
            if j >= n - i - 1 and j < n - 1:
                print(k ,end = "")
                k += 1
            elif j == n - 1:
                k = 2 * i + 1
                print(k,end = "")
                k -= 1
            elif j > n - 1:
                print(k,end = "")
                k -= 1
    print()


