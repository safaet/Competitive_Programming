from collections import defaultdict
class Solution1:
    def majorityElement(self, nums):
        n = len(nums)
        nums.sort()
        
        return nums[n//2]
    


class Solution2:  # Hash Map

    def majorityElement(self, nums):
        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[int] += 1

        n = n//2
        for key, value in m.items():
            if value > n:
                return key
            
        return 0





li = [2, 3, 3]
sol = Solution2()

ans = sol.majorityElement(li)

print(ans)