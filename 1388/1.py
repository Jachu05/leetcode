from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        my_size = 0

        while slices:
            max_num = max(slices)
            max_num_index = slices.index(max_num)

            my_size += max_num

            if max_num_index == len(slices) - 1:
                slices.pop(0)
                max_num_index -= 1
            else:
                slices.pop(max_num_index + 1)

            if max_num_index == 0:
                slices.pop(-1)
            else:
                slices.pop(max_num_index - 1)
                max_num_index -= 1

            slices.pop(max_num_index)

        return my_size


slices = [4, 1, 2, 5, 8, 3, 1, 9, 7]
slices = [21,23,54,34,54,76,54,22,23,1,2,3,4,5,6,54,34,76,4,54,2]
xd = Solution().maxSizeSlices(slices)
