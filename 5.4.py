
import math

class Solution:
    def check(self, n):
        res = []
        y = n
        x = int(math.log10(n) + 1)
        if x == 1:
            return 0
        c = 0
        while (y > 0):
            r = y % 10
            res.append(r)
            y = y // 10
        for i in range(x - 1):
            if abs(res[i] - res[i + 1]) == 1:
                c += 1
        if c == x - 1:
            return 1
        return 0

    def getDigitDiff1AndLessK(self, arr, n, k):
        ans = []
        for i in range(n):
            if arr[i] < k and self.check(arr[i]):
                ans.append(arr[i])
        return ans
print(getDigitDiff1andLessk[7, 98, 56, 43, 45, 23, 12, 8],8,54)
