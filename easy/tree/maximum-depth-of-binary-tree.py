# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _calculate(self, node, level):
        if not node.left and not node.right:
            return level

        left_level = 0
        right_level = 0
        if node.left:
            left_level = self._calculate(node.left, level + 1)

        if node.right:
            right_level = self._calculate(node.right, level + 1)

        return max(left_level, right_level)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._calculate(root, 1)


root = TreeNode(3, TreeNode(9, TreeNode(None), TreeNode(None)), TreeNode(20, TreeNode(15), TreeNode(7)))

sol = Solution()
print(sol.maxDepth(root))
