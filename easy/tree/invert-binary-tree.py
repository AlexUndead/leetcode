from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_leaf(self, node):
        return not node.left and not node.right

    def _invert_tree(self, node):
        if node.left and not self._is_leaf(node.left):
            self._invert_tree(node.left)

        if node.right and not self._is_leaf(node.right):
            self._invert_tree(node.right)

        node.left, node.right = node.right, node.left
            

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            self._invert_tree(root)
            return root


tree = TreeNode(5, left=TreeNode(2, left=TreeNode(1), right=TreeNode(3, right=TreeNode(4))), right=TreeNode(7, left=TreeNode(6), right=TreeNode(9)))
sol = Solution()
a = sol.invertTree(tree)

