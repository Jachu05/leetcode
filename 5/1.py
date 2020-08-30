class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        def check_palind(n, m, local_lcs):
            while n >= 0 and m < len(s):
                if s[n] == s[m]:
                    local_lcs = s[n] + local_lcs + s[m]
                    n -= 1
                    m += 1
                else:
                    break
            return local_lcs

        max_lcs = ''
        for x in range(len(s) - 1):
            lcs1 = check_palind(x, x + 1, '')
            lcs2 = check_palind(x, x + 2, s[x + 1])

            max_lcs = max(max_lcs, lcs1, lcs2, key=len)
        return max_lcs


s = "a"
print(Solution().longestPalindrome(s), 'a')
print()

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
