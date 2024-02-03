from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        find = set()

        for edge in edges:
            if not find:
                find = set(edge)
            else:
                find = find.intersection(edge)


        return find.pop()


sol = Solution()
print(sol.findCenter([[1,2],[2,3],[4,2]]))
