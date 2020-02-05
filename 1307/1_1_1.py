class Solution:
    def isSolvable(self, words, result):
        words.append(result)
        w_max_len = max([len(i) for i in words])
        non_zero_letters = {i[0] for i in words}
        words_len = len(words)

        cache = {k: None for k in set(''.join(words))}
        taken_values = set()

        def rec_wor(word_num, letter_num, count):

            if letter_num >= w_max_len:
                return count == 0

            if word_num >= words_len:
                if not count % 10:
                    return rec_wor(0, letter_num + 1, count // 10)
                else:
                    return False

            word = words[word_num]
            if letter_num >= len(word):
                return rec_wor(word_num + 1, letter_num, count)

            letter = word[~letter_num]
            sign = 1 if word_num < words_len - 1 else -1

            if cache[letter] is None:
                for i in range(10):
                    if (i or letter not in non_zero_letters) and i not in taken_values:
                        cache[letter] = i
                        taken_values.add(i)

                        if rec_wor(word_num + 1, letter_num, count + sign * i):
                            return True

                        taken_values.remove(i)
                        cache[letter] = None

            elif cache[letter] is not None:
                return rec_wor(word_num + 1, letter_num, count + sign * cache[letter])

            return False

        o = rec_wor(0, 0, 0)
        return o


words = ["SEND", "MORE"]
result = "MONEY"
print(Solution().isSolvable(words, result), 'True')

words = ["SIX", "SEVEN", "SEVEN"]
result = "TWENTY"
print(Solution().isSolvable(words, result), 'True')

words = ["THIS", "IS", "TOO"]
result = "FUNNY"
print(Solution().isSolvable(words, result), 'True')

words = ["LEET", "CODE"]
result = "POINT"
print(Solution().isSolvable(words, result), 'False')
