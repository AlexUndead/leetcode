import pdb
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        pdb.set_trace()

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses

sol = Solution()
assert sol.canFinish(5, [[1,4], [2,1], [3,2], [4,1]]) == False
#assert sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]) == True #?

# Мое решение после просмотра ответа
#class Solution:
#    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#        if not prerequisites:
#            return True
#
#        graph = {curse: [] for curse in range(numCourses)}
#
#        for master, slave in prerequisites:
#            graph[slave].append(master)
#
#        path = set()
#        visit = set()
#
#        def has_cycle(node):
#            if node in path:
#                return True
#            if node in visit:
#                return False
#            visit.add(node)
#            path.add(node)
#
#            for slave in graph[node]:
#                if has_cycle(slave):
#                    return True
#
#            path.remove(node)
#            return False
#
#        for i in graph:
#            if has_cycle(i):
#                return False
#
#        return True


#sol = Solution()
#assert sol.canFinish(1, []) == True
#assert sol.canFinish(2, [[1,0]]) == True
#assert sol.canFinish(2, [[1,1]]) == False
#assert sol.canFinish(2, [[1,0], [0,1]]) == False
#assert sol.canFinish(5, [[1,4], [2,1], [3,2], [4,1]]) == False
#assert sol.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]) == True #?
#
#pdb.set_trace()
#assert sol.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]) == False 

