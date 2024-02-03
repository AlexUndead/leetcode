from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _obhod(self, node: TreeNode, path):
        if node.left:
            self._obhod(node.left, path)

        path.append(node.val)

        if node.right:
            self._obhod(node.right, path)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        path = []
        if root:
            self._obhod(root, path)
        return path


tree = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
tree_2 = None
tree_3 = TreeNode(1)
sol = Solution()
print(sol.inorderTraversal(tree))
print(sol.inorderTraversal(tree_2))
print(sol.inorderTraversal(tree_3))
        
