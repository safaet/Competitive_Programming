'''Problem Link: https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''
import math
class Solution:
    def sumOfDivisors(self, N):
        # code here
        sum = 0
        for i in range(1, N+1):
            sum += (N//i) * i
                    
        return sum
    
print(Solution().sumOfDivisors(1))