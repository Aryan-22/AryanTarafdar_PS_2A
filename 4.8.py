def gcd(a,b):
    if a == 1 or b == 1:
        return 1
    if a == b:
        return a
    x ,y = max(a,b),min(a,b)
    return gcd(x - y,y)
a = int(input())
b = int(input())
print(gcd(a,b))