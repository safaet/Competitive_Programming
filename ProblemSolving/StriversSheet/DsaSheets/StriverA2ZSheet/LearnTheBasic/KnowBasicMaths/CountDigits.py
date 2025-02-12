'''
Problem Link: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


class Solution:
    def evenlyDivides (self, N):
        cnt = 0
        n= str(N)
        
        for i in n:
            if int(i) ==0:
                continue
            elif N%int(i) == 0:
                cnt = cnt+1
            
        return cnt
    
sol = Solution()

print(sol.evenlyDivides(2446))
