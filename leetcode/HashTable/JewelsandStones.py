class Solution:

    def numJewelsInStones(self, jewels, stones):
        dic = {}

        for jewel in jewels:
            dic[jewel] = 0

        for stone in stones:
            if stone in dic:
                dic[stone] +=1

        return sum(dic.values())
    


ans = Solution()

print(ans.numJewelsInStones('aA', 'aAAbbbb'))