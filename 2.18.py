class Solution:
    def triDownwards(self, S):
        l = [S]
        for i in range(len(S) - 1):
            s = ""
            for j in range(i + 1):
                s += "."
            l.append(s + S[i + 1:])
        return "".