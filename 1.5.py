def isleap(y):
    return (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0)
def daysm(y,m, k = 1):
    if m == k:
        return 0
    if k == 2:
        if isleap(y):
            return 29 + daysm(y,m,k + 1)
        return 28 + daysm(y,m,k + 1)
    else:
        if (k & 1 and k < 8) or k == 8 :
            return 31 + daysm(y,m,k + 1)
        elif (k & 1  == 0 and k > 8):
            return 31 + daysm(y,m,k + 1)
        return 30 + daysm(y,m,k + 1)

def daysy(y,k = 1500):
    if y > k:
        if isleap(k):
            return 366 + daysy(y,k + 1)
        else:
            return 365 + daysy(y,k + 1)
    return 0

l = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
d = int(input())
m = int(input())
y = int(input())
print(l[(daysy(y) + daysm(y,m) + d - 1) % 7])
