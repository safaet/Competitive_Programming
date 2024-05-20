class Solution:
    def evenlyDivides (self, N):
        cnt = 0
        n= N
        
        while n>0:
            r = n % 10
            # print(r)
            if N % r == 0:
                cnt = cnt + 1
            n = n//10
            
        return cnt
    
sol = Solution()

print(sol.evenlyDivides(2446))
    