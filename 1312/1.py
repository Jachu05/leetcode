from collections import Counter
from math import floor
from re import finditer


class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        rev_s = s[::-1]

        array = [[0] * (s_len + 1) for x in range(2*s_len)]

        for i in range(s_len):
            for j in range(s_len):
                s[i:j + 1]

        print()




# s = "mbadm"
# print(Solution().minInsertions(s), 2)
# #
s = "zzazz"
print(Solution().minInsertions(s), 0)
#
# s = "leetcode"
# print(Solution().minInsertions(s), 5)
# #
# s = "g"
# print(Solution().minInsertions(s), 0)
#
# s = "no"
# print(Solution().minInsertions(s), 1)

# s = "hbbhhh"
# print(Solution().minInsertions(s), 2)

s = "hbaabhh"
print(Solution().minInsertions(s), 1)

s = "hgfedcbaabcdefghh"
print(Solution().minInsertions(s), 1)
#
# s = "tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"
# print(Solution().minInsertions(s), 25)


string = 'aaaaaaaassddds'

# most_common = Counter(string).most_common(1)
# most_common_ch = most_common[0][0]
# most_common_ch_num = most_common[0][1]
#
# x = finditer(most_common_ch, string)
# x2 = [i.regs[0][0] for i in x]
