def nthOfSeries(n):
    # code here
    if n == 1:
        return 9
    return 9 + 8 * (n ** 2 - 8)
print(nthOfSeries(4))