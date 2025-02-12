# Link:
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word):
        ans = 0
        li = [0]*123

        for w in word:
            a = ord(w)
            li[a] = li[a]+1
                
        for l in range(91):
            if li[l]!=0 and li[l+32]!=0:
                ans = ans+1
                
        return ans
    

a = Solution().numberOfSpecialChars('sAfaet')
print(a)