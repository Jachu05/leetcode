class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        cache = {}
        def rec_comp(str1, str2, curr):
            key = (str1, str2)

            # if key in cache:
            #     return cache[key]

            if not str1:
                return str2 + curr
            if not str2:
                return str1 + curr

            if str1[-1] == str2[-1]:
                cache[key] = rec_comp(str1[:-1], str2[:-1], str1[-1] + curr)
            else:
                curr1 = rec_comp(str1, str2[:-1], str2[-1] + curr)
                curr2 = rec_comp(str1[:-1], str2, str1[-1] + curr)
                if len(curr1) < len(curr2):
                    cache[key] = curr1
                else:
                    cache[key] = curr2

            return cache[key]

        xd = rec_comp(str1, str2, '')
        return xd


# str1 = "a"
# str2 = "b"
# print(Solution().shortestCommonSupersequence(str1, str2), 'ab')
#
# str1 = "ad"
# str2 = "ab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'adb')
#
# str1 = "abcc"
# str2 = "cab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabcc')
#
# str1 = "abac"
# str2 = "cab"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')

str1 = "bbbaaaba"
str2 = "bbababbb"
ans = Solution().shortestCommonSupersequence(str1, str2)
print(ans, ans == "bbabaaababb")

# str1 = "asdasdasdasdasdasdasdasdasdasdasdasdasdasdas"
# str2 = "qweqweqweqweqweqweqweqweqweqweqweqweqweqweqw"
# print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')