
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

class Solution:
    def minJumps(self, arr, n):

        jump = 0
        ans = 0
        i = 0
        
        while(i<n):
            print("initial i =", i)
            if i>0:
                ans += 1

            jump = arr[i]
            print("jump =", jump)

            if jump == 0:
                return -1

            i = i+jump
            print("i =", i)
            if i>=n:
                return ans+1
            

        return ans
    

n = int(input())
s = input()
arr = list(map(int, s.split()))
print(arr)
    
print(Solution().minJumps(arr, n))