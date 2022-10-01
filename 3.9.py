class Solution:
    def printPattern(self, N):
    	#code here
    	for i in range(N):
    	    for j in range(i + 1):
    	        print("*",end = "")
    	    print(end = " ")

