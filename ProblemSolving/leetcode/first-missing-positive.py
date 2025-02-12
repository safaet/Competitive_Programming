'''
Problem Link:
https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26

'''


class Solution:
    def firstMissingPositive(self, nums):
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)
        
        # Place each positive integer i at index i-1 if possible
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


nums = [1, 2, 0]

sol = Solution()

print(sol.firstMissingPositive(nums))