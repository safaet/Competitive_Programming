'''
Problem Link: https://www.geeksforgeeks.org/problems/count-digits5716/1
'''

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
    