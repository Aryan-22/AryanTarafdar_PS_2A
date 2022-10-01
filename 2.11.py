n = int(input())
for i in range(n):
    k = i + 1
    for j in range(2 * n):
        if j <= i:
            print(k,end = "")
            k += 1
        elif j >= 2 * n - i - 1:
            k -= 1
            print(k,end = "")
        else:
            print(end = " ")

    print()


