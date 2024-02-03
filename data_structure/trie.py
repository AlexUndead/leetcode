from typing import Union

class TrieNode:
    key = None
    value = None
    is_sheet = False

    def __init__(self, key, children, value=None, is_sheet=False):
        self.key = key
        self.value = value
        self.is_sheet = is_sheet
        self.children = children

class Trie:
    root = TrieNode("", {})

    def add_prefix(self, _str, value) -> None:
        if _str:
            node = self.add_node(_str[-len(_str)], parent_node=self.root)
            for i in _str[1:len(_str)-1]:
                node = self.add_node(i, parent_node=node)
            self.add_node(
                _str[len(_str)-1],
                parent_node=node,
                value=value,
                is_sheet=True
            )

    def search_prefix(self, _str) -> Union[int, bool]:
        if _str:
            node = self.search_node(_str[-len(_str)], node=self.root)
            for i in _str[1:]:
                if not node:
                    return False
                node = self.search_node(i, node=node)
            if node.is_sheet:
                return node.value
            
            return False

    def remove_prefix(self, _str) -> None:
        if _str:
            node = self.search_node(_str[-len(_str)], node=self.root)
            for i in _str[1:]:
                if node:
                    node = self.search_node(i, node=node)
            node.value = None
            node.is_sheet = False

    def search_node(self, key, node) -> Union[TrieNode, bool]:
        if not key in node.children:
            return False
        return node.children[key]

    def add_node(self, key, parent_node, value=None, is_sheet=False) -> TrieNode:
        if not key in parent_node.children:
            node = TrieNode(key, {}, value, is_sheet)
            parent_node.children[key] = node
        else:
            node = parent_node.children[key]

        return node


trie = Trie()
trie.add_prefix("cat", 1)
trie.add_prefix("car", 2)
assert trie.search_prefix("ca") == False
assert trie.search_prefix("car") == 2
trie.remove_prefix("car")
assert trie.search_prefix("car") == False
