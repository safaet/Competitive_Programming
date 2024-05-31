class Solution:
    def fib(self, n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.fib(n-1) + self.fib(n-2)
    

print(Solution().fib(3)) # 34