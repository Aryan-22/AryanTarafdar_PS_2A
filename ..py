l=input().split()
z=[int(i) for i in l]
c=z[0]**z[1]
d=z[1]**z[0]
if(c>d):
    print("First")
elif(d>c):
    print("Second")
elif(c==d):
    print("Equal")
else:
    print("wrong input")