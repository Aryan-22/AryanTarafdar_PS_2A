def lowestTriangle(trianglebase, area):
    i = 0
    while(True):
        if 0.5 * trianglebase * i >= area:
            return i
        i += 1
print(lowestTriangle(2,4))