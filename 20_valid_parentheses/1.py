class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_hash = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for i in s:
            if i in paren_hash:
                stack.append(i)
            elif stack and i == paren_hash[stack[-1]]:
                stack.pop(-1)
            else:
                return False
        return not stack


if '__main__' == __name__:
    print(Solution().isValid("()[]{}"), True)
    print(Solution().isValid("["), False)
    print(Solution().isValid("]"), False)
    print(Solution().isValid("(("), False)
    print(Solution().isValid(")[]{}"), False)
    print(Solution().isValid("(]"), False)
    print(Solution().isValid("([)]"), False)
    print(Solution().isValid("{([])}"), True)
