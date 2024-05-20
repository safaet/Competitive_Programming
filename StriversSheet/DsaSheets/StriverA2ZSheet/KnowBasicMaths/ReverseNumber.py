'''Problem Link: https://leetcode.com/problems/reverse-integer/

'''

class Solution:
    def reverse(self, x):
        n = abs(x)
        RevNum = 0
        while n>0:
            ld = n % 10

            RevNum = (RevNum*10) + ld

            n = n//10

            if RevNum > 2**31 -1:
                return 0

        if x < 0:
            return -1*RevNum
        else:
            return RevNum
    
print(Solution().reverse(1534236469))