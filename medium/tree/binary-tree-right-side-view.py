from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        if root:
            nodes.append(root)
        levels = []

        while nodes:
            level = []
            new_nodes = []
            for node in nodes:
                level.append(node.val)

                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)

            levels.append(level)
            nodes = new_nodes


        return [nodes[-1] for nodes in levels]


sol = Solution()
print(sol.rightSideView(TreeNode(1, left=TreeNode(2, right=TreeNode(5)), right=TreeNode(3, right=TreeNode(4)))))
print(sol.rightSideView(TreeNode(1, right=TreeNode(3))))
print(sol.rightSideView(TreeNode(1, left=TreeNode(2))))
print(sol.rightSideView(None))
