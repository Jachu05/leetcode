from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # (nums[i] - 1) * (nums[j] - 1)
        max_val = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if i != j:
                    temp = (nums[i] - 1) * (nums[j] - 1)
                    if temp > max_val:
                        max_val = temp
        return max_val


nums = [3, 4, 5, 2]
xd = Solution().maxProduct(nums)
