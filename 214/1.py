
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        array = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
        xd = ''
        lcs = ''

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[~j]:
                    array[i + 1][j + 1] = array[i][j] + 1
                else:
                    array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])

        n = len(s)
        m = len(s)
        while array[n][m] != 0:

            if array[n][m] == array[n - 1][m]:
                xd = s[n - 1] + xd
                n -= 1
            elif array[n][m] == array[n][m - 1]:
                xd = s[m - 1] + xd
                m -= 1
            else:
                xd = s[n - 1] + xd
                lcs = s[n - 1] + lcs
                n -= 1
                m -= 1

        xd = s[:n] + xd
        xd = s[:m] + xd

        return xd


s = "aacecaaa"
print(Solution().shortestPalindrome(s), 'aaacecaaa')
print()

s = "abcd"
print(Solution().shortestPalindrome(s), 'dcbabcd')
print()