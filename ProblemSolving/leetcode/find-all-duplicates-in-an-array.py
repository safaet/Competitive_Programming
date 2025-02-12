# Problem Link:
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/?envType=daily-question&envId=2024-03-25

class Solution:
    def findDuplicates(self, nums):
        li = [0] * (len(nums) +1)
        ans= []

        for num in nums:
            li[num] = li[num] + 1

        for i in range(len(li)):
            if li[i] > 1:
                ans.append(i)
                

        return ans
    
num = [4,3,2,7,8,2,3,1]
sol = Solution()

print(sol.findDuplicates(num))