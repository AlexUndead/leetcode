import pdb
from typing import List
from collections import deque
from queue import PriorityQueue


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        max_diff = 0
        visits = set()
        H = len(heights)
        W = len(heights[0])
        queue = PriorityQueue()
        next_coordinate = ([0,1], [1,0])

        queue.put((heights[0][0], (0,0,0)))

        def valid_coord(row, col):
            return 0 <= row < H and 0 <= col < W

        while (H-1, W-1) not in visits:
            cost, coord = queue.get()
            row, col, pre_cost = coord
            visits.add((row, col))
            diff = abs(pre_cost - heights[row][col])
            max_diff = max(max_diff, diff)
            #pdb.set_trace()

            for new_row, new_col in next_coordinate:
                new_row += row
                new_col += col
                if valid_coord(new_row, new_col):
                    queue.put((heights[new_row][new_col] - heights[row][col], (new_row, new_col, heights[row][col])))

        return max_diff



sol = Solution()
print(sol.minimumEffortPath([[1,2,2],[3,8,2],[5,3,5]]))
