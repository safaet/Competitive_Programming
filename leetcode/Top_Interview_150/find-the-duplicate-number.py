class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        li = [0] * len(nums)
        ans= 0

        for num in nums:
            li[num] ++

        for num in li:
            if li[num] > 1:
                ans = num
                break

        return ans


