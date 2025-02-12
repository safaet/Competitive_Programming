'''Problem Link: https://www.geeksforgeeks.org/problems/print-gfg-n-times/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-gfg-n-times
'''

class Solution:
    
    def printGfg(self, n):
        if n == 0:
            return
        self.printGfg(n-1)
        print("GFG", end=" ")

        return


print(Solution().printGfg(5))