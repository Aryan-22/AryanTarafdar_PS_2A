import math
def dsum(k):
    if k == 0:
        return 0
    r = k % 10
    return r + dsum(k // 10)
def onedig(k):
    if int(math.log10(k)) + 1 == 1:
        return k
    return onedig(dsum(k))
print(onedig(98))