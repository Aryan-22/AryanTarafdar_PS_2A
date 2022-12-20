n = input()
x = ""
for i in range(len(n)):
    if n[i].isalpha() and ord(n[i]) <= 91:
        x += chr(ord(n[i]) + 32)

    elif n[i].isalpha() and ord(n[i]) >= 97:
        x += chr(ord(n[i]) - 32)
    else:
        x += n[i]
print(x)