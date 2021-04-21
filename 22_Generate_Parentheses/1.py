from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []

        def is_current_p_can_be_proceeded(current_p: str, max_len: int):
            counter = 0
            for elem in current_p:
                if elem == '(':
                    counter += 1
                else:
                    counter -= 1
                if counter < 0 or counter > max_len:
                    return counter, False
            return counter, True

        def add_parentheses(i: int, current_p: str, max_len: int, all_possible_p: List[str]):
            counter, f_can_be_proceeded = is_current_p_can_be_proceeded(current_p, max_len)
            if not f_can_be_proceeded:
                return False

            if i >= n*2:
                if counter == 0:
                    all_possible_p.append(current_p)
                return

            add_parentheses(i+1, current_p + '(', max_len, all_possible_p)
            add_parentheses(i+1, current_p + ')', max_len, all_possible_p)

        add_parentheses(1, '(', n, stack)
        return stack


if '__main__' == __name__:
    res = Solution().generateParenthesis(1)
    exp = ["()"]
    print(res, exp, set(res) == set(exp))

    res = Solution().generateParenthesis(2)
    exp = ["(())", "()()", ]
    print(res, exp, set(res) == set(exp))

    res = Solution().generateParenthesis(3)
    exp = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print(res, exp, set(res) == set(exp))
