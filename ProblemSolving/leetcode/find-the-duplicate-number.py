class Solution:
    def findDuplicate(self, nums):
        li = [0] * len(nums)
        ans= 0

        for num in nums:
            li[num] = li[num] + 1

        for num in nums:
            if li[num] > 1:
                ans = num
                break

        return ans


num = [1, 2, 3, 3, 3]
sol = Solution()

print(sol.findDuplicate(num))

