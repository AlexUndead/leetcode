import pdb
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    _max_sum = float("-inf")

    def _maxPathSum(self, node):
        if not node.left and not node.right:
            self._max_sum = max(self._max_sum, node.val)
            return node.val

        _all_sum = node.val
        _val_sides = []
        _sum_sides = []

        if node.left:
            left_sum = self._maxPathSum(node.left)
            _val_sides.append(left_sum)
            _sum_sides.append(left_sum + node.val)
            _all_sum += left_sum

        if node.right:
            right_sum = self._maxPathSum(node.right)
            _val_sides.append(right_sum)
            _sum_sides.append(right_sum + node.val)
            _all_sum += right_sum

        self._max_sum = max(self._max_sum, *_val_sides, *_sum_sides, _all_sum, node.val)
        return max(*_sum_sides, node.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self._maxPathSum(root)
        return int(self._max_sum)


sol = Solution()
root = TreeNode(-10, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(sol.maxPathSum(root))
sol = Solution()
root = TreeNode(1, left=TreeNode(-2, left=TreeNode(1, left=TreeNode(-1)), right=TreeNode(3)), right=TreeNode(-3, left=TreeNode(-2), right=TreeNode(0)))
print(sol.maxPathSum(root))
sol = Solution()
root = TreeNode(2, left=TreeNode(-1))
print(sol.maxPathSum(root))
sol = Solution()
root = TreeNode(-1, left=TreeNode(5, left=TreeNode(4, left=TreeNode(-4)), right=TreeNode(0)), right=TreeNode(0, left=TreeNode(0), right=TreeNode(2)))
print(sol.maxPathSum(root))
