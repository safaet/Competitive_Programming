'''https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1
'''

class Solution:
    
    def lcmAndGcd(self, A, B):
        a, b = A, B

        if B>A:
            temp = B
            B = A
            A = temp

        while A:
            A, B = B%A, A

        lcm = (a*b)//B

        return lcm, B
    
print(Solution().lcmAndGcd(405448323, 435638250))