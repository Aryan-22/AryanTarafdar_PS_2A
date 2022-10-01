def med(l):
    n = len(l)
    a = l.sort()
    if n & 1:
        return l[n // 2]
    return l[n // 2 - 1] ,l[n // 2]
def mean(l):
    n = len(l)
    return sum(l) / n

print(med([1,2,3,4,5]),mean([1,2,3,4,5]))