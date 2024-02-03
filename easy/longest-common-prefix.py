import pdb
from typing import List


# Решил быстро. Не проверил все пограничные условия (с пустой строкой).
# В подсказках узнал что нужно было решать через нагруженное дерево
# Нужно переписать через нагруженное дерево
class Solution:
    def get_prefix(self, result, _str):
        res = ""
        for c, i in enumerate(result):
            try:
                if i == _str[c]:
                    res += i
                else:
                    break
            except IndexError:
                break

        return res

    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for j in strs:
            if not j:
                return ""
            if not result:
                result = j
                continue

            result = self.get_prefix(result, j)

            if not result:
                return ""

        return result

sol = Solution()
#print(sol.longestCommonPrefix(["flower","flow","flight"]))
#print(sol.longestCommonPrefix(["dog","racecar","car"]))
print(sol.longestCommonPrefix(["","b"]))

