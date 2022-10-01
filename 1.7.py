t = int(input())
if t < 0:
    print("Freezing weather")
elif 0 <= t < 10:
    print("Very cold weather")
elif 10 <= t < 20:
    print("Cold weather")
elif 20 <= t < 30:
    print("normal")
elif 30 <= t < 40:
    print("Hot")
elif t >= 40:
    print("Very hot")
