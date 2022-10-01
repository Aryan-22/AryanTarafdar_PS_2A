
class Solution:
    def pattern(self, N):
        K = N
        L = []
        while(N > 0):
            L.append(N)
            N -= 5
        while (N <= K):
            L.append(N)
            N += 5
        return L