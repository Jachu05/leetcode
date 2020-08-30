from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        i = 0
        max_i = len(ratings) - 1
        addings_for = [1 for _ in ratings]
        addings_bac = [1 for _ in ratings]

        # foward and bkaward approach
        addings_for[0] = 1
        for i in range(1, max_i + 1):
            if ratings[i] > ratings[i - 1]:
                addings_for[i] = addings_for[i - 1] + 1
            else:
                addings_for[i] = 1

        addings_bac[-1] = 1
        for i in range(max_i - 1, -1, -1):
            if ratings[i] > ratings[i + 1]:
                addings_bac[i] = addings_bac[i + 1] + 1
            else:
                addings_bac[i] = 1

        return sum([max(x, y) for x, y in zip(addings_for, addings_bac)])


ratings = [1,2,2]
xd = Solution().candy(ratings)
