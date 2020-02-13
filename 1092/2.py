class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        c2 = {'min_str': '',
              'min_min': 10000}
        cache = {}

        def rec_comp(str1, str2, c):
            key = (str1, str2)

            if key in cache:
                return cache[key]

            if not str1:
                return str2
            elif not str2:
                return str1

            # c += 1
            # if c > c2['min_min']:
            #     return c2['min_str']

            if str1[-1] == str2[-1]:
                cache[key] = rec_comp(str1[:-1], str2[:-1], c) + str1[-1]
            else:
                curr1 = rec_comp(str1, str2[:-1], c) + str2[-1]
                curr2 = rec_comp(str1[:-1], str2, c) + str1[-1]
                if len(curr1) < len(curr2):
                    cache[key] = curr1
                else:
                    cache[key] = curr2

            c2['min_str'] = cache[key]
            c2['min_min'] = len(cache[key])

            return cache[key]

        xd = rec_comp(str1, str2, 0)
        return xd

str1 = "ab"
str2 = "ad"
print(Solution().shortestCommonSupersequence(str1, str2), 'abad')

str1 = "ab"
str2 = "c"
print(Solution().shortestCommonSupersequence(str1, str2), 'abc')

str1 = "abcc"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2), 'cabcc')

str1 = "abac"
str2 = "cab"
print(Solution().shortestCommonSupersequence(str1, str2), 'cabac')

str1 = "bbbaaaba"
str2 = "bbababbb"
ans = Solution().shortestCommonSupersequence(str1, str2)
print(ans, ans == "bbabaaababb")