from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        i = 0
        max_i = len(ratings) - 1
        addings = [1 for _ in ratings]
        f_continue = True

        if max_i == 0:
            return 1

        while True:
            if (ratings[i] > ratings[i + 1]) and (addings[i] <= addings[i + 1]):
                addings[i] = addings[i + 1] + 1
                f_continue = True
            elif (ratings[i] < ratings[i + 1]) and (addings[i] >= addings[i + 1]):
                addings[i + 1] = addings[i] + 1
                f_continue = True

            if i == max_i - 1:
                i = -1
                if f_continue:
                    f_continue = False
                else:
                    break

            i += 1

        return sum(addings)


ratings = [4,3,3,0,1]
xd = Solution().candy(ratings)
