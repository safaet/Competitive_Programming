'''
Problem Link: https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1
'''
import sys
sys.setrecursionlimit(10**6)
class Solution:

    def sumOfSeries(self, n):
        
        if n == 1:
            return 1
        return n**3 + self.sumOfSeries(n-1)
    
print(Solution().sumOfSeries(18468)) # 225
