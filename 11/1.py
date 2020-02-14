from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        n = 0
        m = len(height) - 1

        max_s = 0
        while n != m:
            left_l = height[n]
            right_l = height[m]

            curr_s = min(left_l, right_l) * (m-n)
            if curr_s > max_s:
                max_s = curr_s

            if left_l < right_l:
                n += 1
            else:
                m -= 1

        return max_s


a = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(a), 49)
