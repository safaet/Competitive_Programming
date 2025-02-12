class Solution:
    def isPalindrome(self, s):
        l = 0
        r = len(s)-1

        while r>l:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True
    
print(Solution().isPalindrome('race a car'))