import pdb
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    isk_root = None

    def search_num(self, node, p, q):
        if p.val < node.val and q.val < node.val:
            self.search_num(node.left, p, q)
        elif p.val > node.val and q.val > node.val:
            self.search_num(node.right, p, q)
        else:
            self.isk_root = node

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        self.search_num(root, p, q)
        return self.isk_root


sol = Solution()
root = TreeNode(6)
root.left=TreeNode(2)
root.left.left=TreeNode(0)
root.left.right=TreeNode(4)
root.left.right.left=TreeNode(3)
root.left.right.right=TreeNode(5)
root.right=TreeNode(8)
root.right.left=TreeNode(7)
root.right.right=TreeNode(9)
print(sol.lowestCommonAncestor(root, TreeNode(3), TreeNode(8)).val)
