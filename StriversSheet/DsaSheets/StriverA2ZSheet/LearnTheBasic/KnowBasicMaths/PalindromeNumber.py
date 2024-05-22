'''Problem Link: https://leetcode.com/problems/palindrome-number/
'''

import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

class Solution:
    
    def isPalindrome(self, x):
        n = x
        RevNum = 0

        while (n>0):
            ld = n%10
            RevNum = (RevNum*10) + ld

            n = n//10

        if RevNum == x:
            return True
        else:
            return False
    

print(Solution().isPalindrome(121))