from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        i = start
        max_i = len(arr)

        cache = set()

        def rec_can(i):
            if i in cache:
                return False

            if i < 0 or i >= max_i:
                return False
            elif arr[i] == 0:
                return True

            move = arr[i]
            cache.add(i)
            o1 = rec_can(i + move)
            o2 = rec_can(i - move)

            if o1 or o2:
                return True
            else:
                return False

        return rec_can(i)


arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

arr = [3, 0, 2, 1, 2]
start = 2

xd = Solution().canReach(arr=arr, start=start)
