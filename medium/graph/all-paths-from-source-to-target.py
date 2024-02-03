import pdb
from typing import List


class Solution:
    def get_path(self, node, path):
        n_path = path[:]
        n_path.append(node)

        if node == len(self.graph) - 1:
            self.pathes.append(n_path)

        for link in self.graph[node]:
            self.get_path(link, n_path)

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = graph
        self.pathes = []

        self.get_path(0, [])

        return self.pathes


sol = Solution()
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
assert sol.allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
assert sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[ 0,1,3,4],[0,1,2,3,4],[0,1,4]]

        
