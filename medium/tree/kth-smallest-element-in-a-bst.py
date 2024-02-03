import pdb
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Есть баг, но ход решения правильный
class Solution:
    result = 0

    def _ob(self, node, k, index):
        if not node.left and not node.right:
            if index == k:
                self.result = node.val
            return index

        if node.left:
            l_index = self._ob(node.left, k, index)
            index += l_index
        
        if index == k:
            self.result = node.val

        if node.right:
            r_index = self._ob(node.right, k, index+1)
            index = r_index

        return index

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self._ob(root, k, 1)
        return self.result
        

sol = Solution()
root = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
print(sol.kthSmallest(root, 4))
root = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
print(sol.kthSmallest(root, 3))
