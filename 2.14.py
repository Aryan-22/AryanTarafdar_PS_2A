name = int(input())                  # Reading input from STDIN
for i in range(name):
    for j in range(name):
        if i == 0 or i == name - 1:
            print("*",end = "")
        elif j == name - i - 1:
            print("*",end = "")
        else:
            print(end = " ")
    print()
                  # Writing output to STDOUT