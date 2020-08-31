from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        end_array = {}

        def rec_check(root, level):
            if root is None:
                return
            if root.val is not None:
                if level in end_array:
                    end_array[level].append(root.val)
                else:
                    end_array[level] = [root.val]

            rec_check(root.left, level + 1)
            rec_check(root.right, level + 1)

        rec_check(root, 0)

        output = [max(array) for array in end_array.values()]

        return output

root = TreeNode(1,
                TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, TreeNode(None), TreeNode(9)))
xd = Solution().largestValues(root)
