class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
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

        return array[-1][-1]


s = "bbbab"
print(Solution().longestPalindromeSubseq(s), 4)
print()

s = "cbbd"
print(Solution().longestPalindromeSubseq(s), 2)
print()
