
class Solution(object):
    def isSolvable(self, words, result):
        words.append(result)
        R, C = len(words), max(map(len, words))

        assigned = {}
        assigned_inv = [None] * 10

        i = 0
        def search(column, row, bal, i):
            i += 1
            # print(i)
            if column >= C:
                return bal == 0
            if row == R:
                return bal % 10 == 0 and search(column + 1, 0, bal // 10, i)

            word = words[row]
            if column >= len(word):
                return search(column, row + 1, bal, i)

            letter = word[~column]
            sign = 1 if row < R - 1 else -1
            if letter in assigned:
                return search(column, row + 1, bal + sign * assigned[letter], i)
            else:
                for d, ad in enumerate(assigned_inv):
                    if ad is None and (d or column != len(word) - 1):
                        assigned_inv[d] = letter
                        assigned[letter] = d
                        if search(column, row + 1, bal + sign * d, i):
                            return True
                        assigned_inv[d] = None
                        del assigned[letter]

            return False

        a = search(0, 0, 0, i)
        return a


words = ["ABD", "B"]
result = "CD"

xd = Solution().isSolvable(words, result)
print(xd)

words = ["AA", "BB"]
result = "AA"

xd = Solution().isSolvable(words, result)
print(xd)

words = ["SIX","SEVEN","SEVEN"]
result = "TWENTY"

xd = Solution().isSolvable(words, result)
print(xd)

words = ["I","THINK","IT","BE","THINE"]
result = "INDEED"

xd = Solution().isSolvable(words, result)
print(xd)

words = ["SEND", "MORE"]
result = "MONEY"
xd = Solution().isSolvable(words, result)
print(xd)

words = ["THIS","IS","TOO"]
result = "FUNNY"
xd = Solution().isSolvable(words, result)
print(xd)

words = ["LEET","CODE"]
result = "POINT"
xd = Solution().isSolvable(words, result)
print(xd)

words = ["TO","BE","OR","NOT"]
result = "TOBE"
xd = Solution().isSolvable(words, result)
print(xd)

words = ["BUT","ITS","STILL"]
result = "FUNNY"
xd = Solution().isSolvable(words, result)
print(xd)

words = ["HOPE","THIS","HELPS","OTHER"]
result = "PEOPLE"
xd = Solution().isSolvable(words, result)
print(xd)
