class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :type s: str
        :rtype: str
        """
        array = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

        n = 0
        xd = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[~j]:
                    # if j == i:
                    #     continue
                    array[i + 1][j + 1] = array[i][j] + 1

                    if array[i + 1][j + 1] > n:
                        n = array[i + 1][j + 1]
                        xd = ''
                        for x in range(n):
                            print(i - 1 - x)
                            xd = s[i - 1 - x] + xd

        return xd



s = "babad"
print(Solution().longestPalindrome(s), 'bab')
print()
#
s = "cbbd"
print(Solution().longestPalindrome(s), 'bb')
print()

s = "abcda"
print(Solution().longestPalindrome(s), 'a')
print()

s = "aacdefcaa"
print(Solution().longestPalindrome(s), 'aa')
print()