'''Problem Link: https://www.geeksforgeeks.org/problems/print-n-to-1-without-loop/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=print-n-to-1-without-loop
'''
class Solution:

    def printNos(self, n):

        if n<=0:
            return
        print(n, end=" ")
        self.printNos(n-1)
        

print(Solution().printNos(10))