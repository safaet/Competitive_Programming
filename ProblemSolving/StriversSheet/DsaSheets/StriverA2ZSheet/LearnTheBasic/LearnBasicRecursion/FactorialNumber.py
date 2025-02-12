class Solution:

    def factorialNumbers(self, N):
        ans = 1
        x = 2
        arr = []
        while ans <= N:
            arr.append(ans)
            ans *= x            
            x += 1
        return arr
    
print(Solution().factorialNumbers(6)) # [1, 2, 6, 24, 120]