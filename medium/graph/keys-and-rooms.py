import pdb
from typing import List
from queue import Queue


# obs = {0:0, 1:0, 2:0}
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set([0])
        queue = Queue()
        for key in rooms[0]:
            queue.put(key)

        while not queue.empty():
            room = queue.get()
            if room in visit:
                continue
            
            visit.add(room)
            for key in rooms[room]:
                queue.put(key)

        return len(visit) == len(rooms)



sol = Solution()
assert sol.canVisitAllRooms([[1],[2],[3],[]]) == True
assert sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False
assert sol.canVisitAllRooms([[4],[3],[],[2,5,7],[1],[],[8,9],[],[],[6]]) == False
