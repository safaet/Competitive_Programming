from collections import Counter

class Solution:


    def shortestCompletingWord(self, licensePlate, words):
        valid = Counter()

        for x in licensePlate:
            x = x.lower()
            if x.isalpha():
                valid[x] += 1
        # valid = Counter("".join(x.lower() for x in licensePlate if x.isalpha()))
        ans = ""

        for word in words:
            j = Counter(word)




ans = Solution()

licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

print(ans.shortestCompletingWord(licensePlate, words))