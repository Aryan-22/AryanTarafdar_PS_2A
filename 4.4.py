'''1 4 9 16 25
if the given no. can be represented as the sum of the first n ** 0.5 odd no.s then it is perfect square
'''
def pf(n):
    s = 0
    i = 0
    while(s < n):
        s += 2 * i + 1
        i += 1
    if s == n:
        return True
    return False

l = int(input())
u = int(input())
for i in range(l,u + 1):
    if pf(i):
        print(i,end = " ")
