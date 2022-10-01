global x
x = []
def rep(n):
    l = [str(n) for i in range(2 * n - 1)]
    return l
def solve(n,l,k = 1):
    if n == k:
        return
    else:
        z = l[:k] + rep(n - k) + l[2 * n - 1 - k:]
        x.append(z)
        k += 1
        return solve(n,z,k)
n = int(input())
l = [str(n) for i in range(2 * n - 1)]
x.append(l)
solve(n,l)
res  = x + x[::-1][1:]
for i in range(len(res)):
    print("".join(res[i]))