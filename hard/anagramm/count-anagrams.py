import pdb
from collections import Counter
from functools import reduce
import operator


# Time Limit Exceeded 
# 36/41
class Solution:
    def fact(self, j: int) -> int:
        if not j:
            return 0
        result = 1
        for i in range(2, j+1):
            result *= i
        return result

    def prod(self, iterable):
        return reduce(operator.mul, iterable, 1)

    def count(self, s: str) -> int:
        if not s:
            return 0

        count = Counter(s)
        result = self.fact(len(s))

        if len(s) != len(count):
            znam = self.prod([self.fact(coun) for key, coun in count.items() if coun > 1])
            result = result//znam

        return result

    def countAnagrams(self, s: str) -> int:
        anagramm = s.split(" ")
        asdf = [self.count(anag) for anag in anagramm]
        return self.prod(asdf)


sol = Solution()
#print(sol.countAnagrams("too hot"))
#print(sol.countAnagrams("oo"))
print(sol.countAnagrams("ptx cccbhbq"))
