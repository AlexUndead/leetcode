from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Решил быстро. Обычный обход в ширину
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        result.append([root.val])
        childrens = [root]

        while childrens:
            child_result = []
            _childrens = childrens[:]
            childrens = []

            for child in _childrens:
                if child.left:
                    childrens.append(child.left)
                    child_result.append(child.left.val)

                if child.right:
                    childrens.append(child.right)
                    child_result.append(child.right.val)

            if child_result:
                result.append(child_result)

        return result

sol = Solution()
root = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(sol.levelOrder(root))
root = TreeNode(val=None)
print(sol.levelOrder(root))
