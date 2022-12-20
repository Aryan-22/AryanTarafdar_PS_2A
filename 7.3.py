def rev(l):
    s = ""
    for i in range(len(l) - 1,-1,-1):
        s += l[i]
    return s
l = input()
x = rev(l)
if x == l:
    print("palindrome!")
else:
    print("not a palindrome")