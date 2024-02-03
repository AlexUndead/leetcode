from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _is_sub(self, tree, subtree):
        if not tree and not subtree:
            return True
        elif not tree or not subtree:
            return False
        else: 
            return tree.val == subtree.val and self._is_sub(tree.left, subtree.left) and self._is_sub(tree.right, subtree.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        childrens = [root]

        while childrens:
            _c = childrens[:]
            childrens = []

            for child in _c:
                if child.left:
                    childrens.append(child.left)

                if child.right:
                    childrens.append(child.right)

                if self._is_sub(child, subRoot):
                    return True
        return False


sol = Solution()
root = TreeNode(3, left=TreeNode(4, left=TreeNode(1), right=TreeNode(2)), right=TreeNode(5))
subroot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
print(sol.isSubtree(root, subroot))
