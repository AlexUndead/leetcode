import pdb


class Tree:
    def __init__(self, tree):
        _iter = iter(tree)
        self.data = next(_iter)
        self.children = [Tree(i) for i in _iter]

    def traversal_tree(self, level=0):
        string = level * " " + str(self)
        level += 1
        for child in self.children:
            string += child.traversal_tree(level)

        return string

    def __str__(self):
        return self.data + "\n"

    def __eq__(self, other):
        return self.traversal_tree() == other.traversal_tree()

    def __contains__(self, k):
        if self.data == k:
            return True

        return any(k in child for child in self.children)

    def height(self, start=0):
        level = start

        for child in self.children:
            child_level = child.height(start + 1)
            if child_level > level:
                level = child_level

        return level

#def traversal_tree(tree):
#    print(tree[0])
#    for children in tree[1:len(tree)]:
#        traversal_tree(children)
#
#def iter_traversal_tree(tree):
#    _iter = iter(tree)
#    print(next(_iter))
#    for children in _iter:
#        iter_traversal_tree(children)

#T = ['c', ['a', ['p'], ['n'], ['t']], ['o', ['n']]]
T = ['a', ['b', ['c', ['d']]],['e',['f'], ['g']]]
T2 = ['a', ['b', ['d', ['d']]],['e',['f'], ['g']]]

tree = Tree(T)
tree2 = Tree(T2)
print(tree == tree2)
print(tree.height())
print("j" in tree)
#pdb.set_trace()
