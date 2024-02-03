import pdb
from typing import List
from queue import Queue

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        cycles = []
        queue = Queue()
        visits = {edge: 0 for edge in range(len(edges))}

        for out in edges:
            if out != -1:
                visits[out] += 1

        for node in visits:
            if not visits[node]:
                queue.put(node)

        while not queue.empty():
            node = queue.get()
            _next = visits.get(edges[node])
            if _next: 
                visits[edges[node]] -= 1
                if not visits[edges[node]]:
                    queue.put(edges[node])

            del visits[node]

        if not visits:
            return -1
            
        while visits:
            vis = set()
            path = []
            node = next(iter(visits.keys()))

            while node not in vis:
                vis.add(node)
                path.append(node)
                node = edges[node]

            cycles.append(len(path))
            for p in path:
                del visits[p]

        return max(cycles)

        
sol = Solution()
print(sol.longestCycle([3,3,4,2,3]))
print(sol.longestCycle([2,-1,3,1]))
print(sol.longestCycle([1,2,0,4,5,6,3,8,9,7]))
