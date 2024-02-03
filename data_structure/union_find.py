import pdb
from typing import Union, List


class UnionFind:
    unions = {}

    def find(self, val:int):# -> Union[None, int]:
        for union in self.unions:
            if val in self.unions[union]:
                return union

    def add(self, val:int) -> None:
        union = self.find(val)
        if not union:
            self.unions[val] = set([val])
        else:
            self.unions[union].add(val)

    def unite(self, unite:List[int]) -> None:
        f_unite = self.find(unite[0])
        s_unite = self.find(unite[1])

        if f_unite is not None and s_unite is not None and f_unite is not s_unite:
            self.unions[f_unite].update(self.unions[s_unite])
            del self.unions[s_unite]

#un = UnionFind()
#un.add(1)
#un.add(2)
#un.add(3)
#un.add(4)
#un.unite([1,2])
#print(un.unions)
#print(un.unions[un.find(1)])
#pdb.set_trace()
