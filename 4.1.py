def pal(n):
    y = n
    s = 0
    while(y > 0):
        r = y % 10
        s = s * 10
        s += r
        y = y // 10
    if s == n:
        return True
    return False

n = int(input())
print(pal(n))
