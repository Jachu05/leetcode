from collections import Counter
from math import floor
from re import finditer


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_rec_d = {}
        s_len = len(s)

        def rec_pal(left, right, curr_rec=0):

            if (left, right) in max_rec_d:
                return max_rec_d[(left, right)]

            if right - left == 0:
                curr_rec += 1

            if s[left] == s[right]:
                if right - left > 1:
                    curr_rec = rec_pal(left + 1, right - 1, curr_rec + 2)
                elif right - left == 1:
                    curr_rec = 2
                # max_rec_d[(left, right)] = curr_rec
            else:
                curr_rec1 = rec_pal(left + 1, right, curr_rec)
                curr_rec2 = rec_pal(left, right - 1, curr_rec)
                curr_rec = max(curr_rec1, curr_rec2)

            print(left, right, curr_rec)

            max_rec_d[(left, right)] = curr_rec
            return curr_rec

        max_pali = rec_pal(0, s_len - 1, 0)

        pali_letters = s_len - max_pali
        return pali_letters


# s = "mbadm"
# print(Solution().minInsertions(s), 2)

s = "zzazz"
print(Solution().minInsertions(s), 0)

# s = "leetcode"
# print(Solution().minInsertions(s), 5)
#
# s = "g"
# print(Solution().minInsertions(s), 0)
#
# s = "no"
# print(Solution().minInsertions(s), 1)
#
# s = "hgfedcbaabcdefghhhh"
# print(Solution().minInsertions(s), 3)

# s = "tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"
# print(Solution().minInsertions(s), 3)


string = 'aaaaaaaassddds'

# most_common = Counter(string).most_common(1)
# most_common_ch = most_common[0][0]
# most_common_ch_num = most_common[0][1]
#
# x = finditer(most_common_ch, string)
# x2 = [i.regs[0][0] for i in x]
