from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Мое решение с генераторами, на leetcode не проходит последний тест, у меня проходит!!!
#class Solution:
#    def _vertical_bypass(self, node):
#        if not node.left and not node.right:
#            yield node.val
#        else:
#            if not node.left and node.right:
#                yield None
#
#            if node.left:
#                yield from self._vertical_bypass(node.left)
#
#            yield node.val
#
#            if node.right:
#                yield from self._vertical_bypass(node.right)
#
#    def vertical_bypass(self, root):
#        if not root:
#            yield None
#        else:
#            yield from self._vertical_bypass(root)
#
#
#    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#        _p = self.vertical_bypass(p)
#        _q = self.vertical_bypass(q)
#
#        for i in _p:
#            try:
#                if i != next(_q):
#                    return False
#            except StopIteration:
#                return False
#
#        try:
#            next(_q)
#        except StopIteration:
#            return True
#        
#        return False
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



sol = Solution()
p = None
q = None
print(sol.isSameTree(p, q))
p = None
q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
print(sol.isSameTree(p, q))
p = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
q = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
print(sol.isSameTree(p, q))
p = TreeNode(1, left=TreeNode(2))
q = TreeNode(1, right=TreeNode(3))
print(sol.isSameTree(p, q))
p = TreeNode(1, left=TreeNode(2), right=TreeNode(1))
q = TreeNode(1, left=TreeNode(1), right=TreeNode(2))
print(sol.isSameTree(p, q))

p = TreeNode(5, left=TreeNode(4, left=TreeNode(None), right=TreeNode(1, left=TreeNode(2))), right=TreeNode(1, left=TreeNode(None), right=TreeNode(4, right=TreeNode(2))))
p = TreeNode(5, left=TreeNode(1, left=TreeNode(4, left=TreeNode(None), right=TreeNode(2))), right=TreeNode(4, left=TreeNode(1, left=TreeNode(None), right=TreeNode(2))))
print(sol.isSameTree(p, q))
