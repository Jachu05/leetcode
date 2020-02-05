height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


class Solution:
    def trap(self, height):
        max_len = len(height)
        diff = 0

        def find_n(h, n):
            c = 0
            while n < len(height) - 1:
                n += 1
                if height[n] >= h:
                    return c
                c += 1
            return 0

        for x in range(len(height)):
            if height[x] >= 1:
                diff += find_n(height[x], x)

        return diff


xd = Solution().trap(height)
