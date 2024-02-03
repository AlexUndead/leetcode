import pdb
from typing import Union


class Node:
    def __init__(self, symb="", is_key=False):
        self.symb = symb
        self.is_key = is_key
        self.childs = []

class Trie:
    def __init__(self):
        self.root = Node()

    def _insert(self, node, symb, is_key=False) -> Node:
        for child in node.childs:
            if child.symb == symb:
                if is_key:
                    child.is_key = True
                return child

        child = Node(symb, is_key)
        node.childs.append(child)

        return child

    def insert(self, word: str) -> None:
        body = word[:-1]
        tail = word[-1]
        prev_node = self.root
        for sym in body:
            prev_node = self._insert(prev_node, sym)
        self._insert(prev_node, tail, is_key=True) 

    def _search(self, node, symb) -> Union[Node, None]:
        for child in node.childs:
            if child.symb == symb:
                return child
        return None
        
    def search(self, word: str) -> bool:
        body = word[:-1]
        tail = word[-1]
        prev_node = self.root

        for symb in body:
            prev_node = self._search(prev_node, symb)
            if not prev_node:
                return False

        last_node = self._search(prev_node, tail)
        is_search = True if last_node and last_node.is_key else False
        return is_search

    def startsWith(self, prefix: str) -> bool:
        prev_node = self.root

        for symb in prefix:
            prev_node = self._search(prev_node, symb)
            if not prev_node:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
#obj = Trie()
#obj.insert("word")
#obj.insert("wost")
#param_2 = obj.search("word")
#param_3 = obj.search("wordd")
#print(param_2)
#print(param_3)
# param_3 = obj.startsWith(prefix)

#obj = Trie()
#obj.insert("apple")
#print(obj.search("apple"))
#print(obj.search("app"))
#print(obj.startsWith("app"))
#obj.insert("app")
#print(obj.search("app"))

obj = Trie()
obj.insert("app")
obj.insert("apple")
obj.insert("beer")
obj.insert("add")
obj.insert("jam")
obj.insert("rental")
print(obj.search("apps"))
print(obj.search("app"))
