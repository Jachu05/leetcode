class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :type s: str
        :rtype: str
        """
        cache = {}
        longest = ''
        def rec_pal(s, n, m, longest):
            key = (n, m)

            if key in cache:
                return cache[key]

            if longest:
                if len(longest) >= len(s):
                    return longest

            if s != s[::-1]:
                curr1 = rec_pal(s[:-1], n, m + 1, longest)
                curr2 = rec_pal(s[1:], n + 1, m, longest)
                if len(curr1) > len(curr2):
                    cache[key] = curr1
                else:
                    cache[key] = curr2
            else:
                longest = s
                cache[key] = s
            return cache[key]

        return rec_pal(s, 0, 0, longest)


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