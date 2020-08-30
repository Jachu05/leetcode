class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()

        def sohappy(number):
            if number in cache:
                return False

            str_num = str(number)
            new_number = 0
            for x in str_num:
                new_number += pow(int(x), 2)
            if new_number > 1:
                cache.add(number)
                return sohappy(new_number)

            return bool(new_number)

        xd = sohappy(n)

        return xd


a = Solution().isHappy(2)
