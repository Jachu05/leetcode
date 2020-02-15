class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :type s: str
        :rtype: str
        """
        cache = {}
        def rec_pal(s):
            if s in cache:
                return cache[s]

            if s != s[::-1]:
                curr1 = rec_pal(s[:-1])
                curr2 = rec_pal(s[1:])
                if len(curr1) > len(curr2):
                    cache[s] = curr1
                else:
                    cache[s] = curr2
            else:
                cache[s] = s
            return cache[s]

        return rec_pal(s)


s = "babad"
print(Solution().longestPalindrome(s), 'bab')
print()

s = "cbbd"
print(Solution().longestPalindrome(s), 'bb')
print()

s = "abcda"
print(Solution().longestPalindrome(s), 'a')
print()

s = "babaddtattarrattatddetartrateedredividerb"
print(Solution().longestPalindrome(s), 'a')
print()