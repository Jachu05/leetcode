import collections
from typing import List
import numpy as np
from itertools import permutations, chain

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        scale = collections.defaultdict(int)
        for word in words:
            n = 1
            for char in word[::-1]:
                scale[char] += n
                n *= 10

        n = 1
        for char in result[::-1]:
            scale[char] -= n
            n *= 10

        scale_values = tuple(scale.values())
        N = len(scale_values)

        def permutations_to_array(r, k):
            it = permutations(r, k)
            arr = np.fromiter(chain.from_iterable(it), dtype = np.int8)
            arr = arr.reshape((-1, N))

            return arr

        xd = permutations_to_array(range(0, 10), N)
        # xd = np.asarray(a1)
        xd2 = np.array(scale_values).reshape(-1, 1)
        res = np.matmul(xd, xd2)
        o = bool(np.argwhere(res == 0).any())

        return o



# words = ["SIX","SEVEN","SEVEN"]
# result = "TWENTY"
#
# xd = Solution().isSolvable(words, result)
# print(xd)
#
# words = ["I","THINK","IT","BE","THINE"]
# result = "INDEED"
#
# xd = Solution().isSolvable(words, result)
# print(xd)
#
# words = ["SEND","MORE"]
# result = "MONEY"
#
# xd = Solution().isSolvable(words, result)
# print(xd)
#
# words = ["THIS","IS","TOO"]
# result = "FUNNY"
# xd = Solution().isSolvable(words, result)
# print(xd)
#
# words = ["LEET","CODE"]
# result = "POINT"
# xd = Solution().isSolvable(words, result)
# print(xd)

# words = ["TO","BE","OR","NOT"]
# result = "TOBE"
# xd = Solution().isSolvable(words, result)
# print(xd)

# words = ["BUT","ITS","STILL"]
# result = "FUNNY"
# xd = Solution().isSolvable(words, result)
# print(xd)

words = ["HOPE","THIS","HELPS","OTHER"]
result = "PEOPLE"
xd = Solution().isSolvable(words, result)
print(xd)