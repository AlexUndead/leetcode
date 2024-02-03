import pdb
from typing import Union


class Node:
    def __init__(self, symb="", is_key=False):
        self.symb = symb
        self.is_key = is_key
        self.childs = []

# Решил.
# Не правильно понял задачу. В след раз читай внимательнее. Нужно проверять на окончание слова, а не возвращать любой похожий патерн
class WordDictionary:
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

    def addWord(self, word: str) -> None:
        body = word[:-1]
        tail = word[-1]
        prev_node = self.root
        for sym in body:
            prev_node = self._insert(prev_node, sym)
        self._insert(prev_node, tail, is_key=True) 

    def _search(self, node, word):
        result = False
        childs = node.childs
        for i, symb in enumerate(word, 1):
            result = False
            new_childs = []

            for child in childs:
                if symb == child.symb or symb == ".":
                    if i == len(word):
                        if child.is_key:
                            return True
                        else:
                            result = False
                    else:
                        result = True
                        new_childs += child.childs

            childs = new_childs

            if not result:
                return False

        return result


    def search(self, word: str) -> bool:
        return self._search(self.root, word)


wd = WordDictionary()
#№1
#wd.addWord("bad")
#wd.addWord("dad")
#wd.addWord("mad")
#print(wd.search("pad"))
#print(wd.search("bad"))
#print(wd.search(".ad"))
#print(wd.search("b.."))

#№2
wd.addWord("a")
wd.addWord("at")
wd.addWord("and")
wd.addWord("an")
wd.addWord("add")
#print(wd.search("a"))
wd.addWord("bat")
#print(wd.search(".at")) #True
#print(wd.search("an.")) #True
#print(wd.search("a.d.")) #False
#print(wd.search("b.")) #False
#print(wd.search("a.d")) #True
print(wd.search(".")) #false
print(wd.search("..")) #True
##print(wd.search("b.."))
