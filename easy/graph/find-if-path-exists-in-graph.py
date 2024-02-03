import pdb
from typing import List
from data_structure.union_find import UnionFind


# Мое решение, оно правильно только не прошло TimeLimit
#class Solution:
#    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#        if not edges:
#            if source == 0 and destination == 0:
#                return True
#            return False
#
#        graph = {}
#        visits = []
#
#        for edge in edges:
#            if not graph.get(edge[0]):
#                graph[edge[0]] = [edge[1]]
#            else:
#                graph[edge[0]].append(edge[1])
#
#            if not graph.get(edge[1]):
#                graph[edge[1]] = [edge[0]]
#            else:
#                graph[edge[1]].append(edge[0])
#
#        def obhod(vert, destination):
#            result = False
#            if vert not in visits:
#                visits.append(vert)
#
#                for child in graph[vert]:
#                    if child != destination:
#                        result = obhod(child, destination)
#                        if result:
#                            break
#                    else:
#                        return True
#            return result
#
#        return obhod(source, destination)
#
#
## Решение на leetcode
#class Solution:
#    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#        graph = collections.defaultdict(list)
#        for a, b in edges:
#            graph[a].append(b)
#            graph[b].append(a)
#            
#        seen = [False] * n
#        
#        def dfs(curr_node):
#            if curr_node == destination:
#                return True
#            if not seen[curr_node]:
#                seen[curr_node] = True
#                for next_node in graph[curr_node]:
#                    if dfs(next_node):
#                        return True
#            return False
#            
#        return dfs(source)

# Решение через UnionFind. На литкоде пример падает на след примере (литкод говорит что у них возвращается true)
#print(sol.validPath(10, [[2,9],[7,8],[5,9],[7,2],[3,8],[2,8],[1,6],[3,0],[7,0],[8,5]], 1, 0))
# локально все ок, хз че там происходит на leetcode

class Solution:
    def __init__(self):
        self.un = UnionFind()

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        for edge in edges:
            self.un.add(edge[0])
            self.un.add(edge[1])
            self.un.unite(edge)

        return destination in self.un.unions[self.un.find(source)]


sol = Solution()
#assert True == sol.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
#assert False == sol.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
assert True == sol.validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[ 0,9],[5,4]], 5, 9)
