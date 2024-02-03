import pdb
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i:[] for i in range(n)}

        for edge in edges:
            out, _in = edge
            graph[_in].append(out)

        return [i for i in graph if not graph[i]]

sol = Solution()
print(sol.findSmallestSetOfVertices(6, [[0,1],[0,2],[2,5],[3,4],[4,2]]))
print(sol.findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]]))
