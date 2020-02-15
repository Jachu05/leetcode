class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :type s: str
        :rtype: str
        """
        array = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[~j]:
                    array[i + 1][j + 1] = array[i][j] + 1
                else:
                    array[i + 1][j + 1] = max(array[i][j + 1], array[i + 1][j])

        n = len(s)
        m = n
        lcs = ''
        while array[n][m] != 0:

            if array[n][m] == array[n - 1][m]:
                n -= 1
            elif array[n][m] == array[n][m - 1]:
                m -= 1
            else:
                lcs = s[n - 1] + lcs
                n -= 1
                m -= 1

        return lcs


# s = "babad"
# print(Solution().longestPalindrome(s), 'bab')
# print()
#
# s = "cbbd"
# print(Solution().longestPalindrome(s), 'bb')
# print()

s = "abcda"
print(Solution().longestPalindrome(s), 'a')
print()
