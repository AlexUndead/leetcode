from typing import List

# Решение не прошло по времени т.к. много перекрытий
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volumes = 0
        cursor_count = 1

        while height:
            cursor = height.pop(0)
            for count, hei in enumerate(height, 1):
                n_count = cursor_count + count
                volume = (n_count - cursor_count) * min(cursor, hei)
                max_volumes = max(max_volumes, volume)

            cursor_count += 1

        return max_volumes


sol = Solution()
assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert sol.maxArea([1,1]) == 1
