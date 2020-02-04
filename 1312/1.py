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

            if right - left == 1:
                return curr_rec

            if s[left] == s[right]:
                max_rec_d[(left, right)] = curr_rec + 2
                curr_rec = rec_pal(left + 1, right - 1, curr_rec + 2)
            else:
                max_rec_d[(left, right)] = 0
                curr_rec1 = rec_pal(left + 1, left, 0)
                curr_rec2 = rec_pal(left, right - 1, 0)
                curr_rec = max(curr_rec1, curr_rec2)

            return curr_rec

        max_pali = rec_pal(0, s_len - 1, 0)

        pali_letters = s_len // 2
        mirror_lett = abs(pali_letters - max_pali)
        to_pali_letters = mirror_lett * 2
        return to_pali_letters


s = "mbadm"
print(Solution().minInsertions(s), 2)

s = "zzazz"
print(Solution().minInsertions(s), 0)

string = 'aaaaaaaassddds'

# most_common = Counter(string).most_common(1)
# most_common_ch = most_common[0][0]
# most_common_ch_num = most_common[0][1]
#
# x = finditer(most_common_ch, string)
# x2 = [i.regs[0][0] for i in x]
