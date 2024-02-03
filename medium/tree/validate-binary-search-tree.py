import pdb
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_valid(self, node):
        if not node.left and not node.right:
            return (node.val, node.val), node.val, True
    
        l_is_valid = r_is_valid = True
        l_val = float("-inf")
        r_val = float("inf")
        valid = True

        if node.left:
            l_min_max, l_val, l_is_valid = self._is_valid(node.left)
            valid = max(l_min_max) < node.val
            if not l_is_valid:
                return (node.val, node.val), node.val, False
        else:
            l_min_max = (node.val,)

        if node.right:
            r_min_max, r_val, r_is_valid = self._is_valid(node.right)
            if valid:
                valid = min(r_min_max) > node.val
            if not r_is_valid:
                return (node.val, node.val), node.val, False
        else:
            r_min_max = (node.val,)

        return (min(l_min_max), max(r_min_max)), node.val, l_val < node.val < r_val and valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        _, _, valid = self._is_valid(root)
        return valid


sol = Solution()
root = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
print(sol.isValidBST(root))
root = TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6)))
print(sol.isValidBST(root))
root = TreeNode(5, left=TreeNode(4), right=TreeNode(6, left=TreeNode(3), right=TreeNode(7)))
print(sol.isValidBST(root))
root = TreeNode(1, left=TreeNode(1))
print(sol.isValidBST(root))
root = TreeNode(0, left=TreeNode(-1))
print(sol.isValidBST(root))
root = TreeNode(34, left=TreeNode(-6, left=TreeNode(-21)))
print(sol.isValidBST(root))
root = TreeNode(3, left=TreeNode(1, left=TreeNode(0), right=TreeNode(2, right=TreeNode(3))), right=TreeNode(5, left=TreeNode(4), right=TreeNode(6)))
print(sol.isValidBST(root))
