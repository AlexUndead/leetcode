from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        _set = set(nums)
        for i, v in enumerate(_set):
            if i == len(nums) - k:
                return v


sol = Solution()
print(sol.findKthLargest([3,2,1,5,6,4], k=2))
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], k=4))

        
