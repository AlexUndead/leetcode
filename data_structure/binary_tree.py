import pdb


class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, values):
        self.root = BinaryNode(values[0])

        for value in values[1:]:
            self.add_node(value)

    def add_node(self, value):
        self._add_node(self.root, value)

    def _add_node(self, node, value):
        if node.value > value and not node.left:
            node.left = BinaryNode(value)
        if node.value < value and not node.right:
            node.right = BinaryNode(value)
        if node.value > value:
            self._add_node(node.left, value)
        if node.value < value:
            self._add_node(node.right, value)

    def horizont_traversal_tree(self):
        a = [self.root]
        print(self.root.value)
        while a:
            node = a.pop(0)
            if node.left:
                print(node.left.value)
                a.append(node.left)
            if node.right:
                print(node.right.value)
                a.append(node.right)

    def remove_node(self, value):
        if self.root.value == value:
            self.root = None
        else:
            self._remove_node(self.root, value)

    def _remove_node(self, node, value):
        if self.check_leaf_node(node):
            return
        if node.left and node.left.value == value and self.check_leaf_node(node.left):
            node.left = None
            return
        elif node.right and  node.right.value == value and self.check_leaf_node(node.right):
            node.right = None
            return
        if node.left and node.left.value == value and self.check_node_with_one_brach(node.left):
            if node.left.right:
                node.left.value = node.left.right.value
                node.left.right = None
                return
            if node.left.left:
                node.left.value = node.left.left.value
                node.left.left = None
                return
        elif node.right and node.right.value == value and self.check_node_with_one_brach(node.right):
            if node.right.left:
                node.right.value = node.right.left.value
                node.right.left = None
                return
            if node.right.right:
                node.right.value = node.right.right.value
                node.right.right = None
                return
        if node.left and node.left.value == value and self.check_node_with_two_brach(node.left):
            pre_max_node, max_node = self.search_max_two_nodes(node.left)
            node.left.value = max_node.value
            if self.check_node_with_one_brach(max_node):
                pre_max_node.right = max_node.left
            else:
                pre_max_node.right = None
            return
        elif node.right and node.right.value == value and self.check_node_with_two_brach(node.right):
            pre_max_node, max_node = self.search_max_two_nodes(node.right.left)
            node.right.value = max_node.value
            if self.check_node_with_one_brach(max_node):
                pre_max_node.right = max_node.left
            else:
                pre_max_node.right = None
            return

        if node.value < value:
            self._remove_node(node.right, value)
        else:
            self._remove_node(node.left, value)
            

    def check_leaf_node(self, node):
        if node:
            return not node.left and not node.right

    def check_node_with_one_brach(self, node):
        if node:
            return (node.left or node.right) and (not node.left or not node.right)

    def check_node_with_two_brach(self, node):
        if node:
            return node.left and node.right

    def search_max_two_nodes(self, node):
        cur = node

        while cur.right.right:
            cur = cur.right

        return cur, cur.right


tree = BinaryTree([6,2,3,8,5,8,9,4])
#tree = BinaryTree([4,8,5,7,6,9])
#tree = BinaryTree([3,2,1,6,4,5,9,8,10])
tree.horizont_traversal_tree()
tree.remove_node(8)
print("hello")
tree.horizont_traversal_tree()

pdb.set_trace()
