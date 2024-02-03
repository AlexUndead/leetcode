from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m_i = m - 1
        n_i = n - 1
        insert_index = len(nums1) - 1

        while n_i >= 0:
            if nums1[m_i] > nums2[n_i] and m_i >= 0:
                nums1[insert_index] = nums1[m_i]
                m_i -= 1
            else:
                nums1[insert_index] = nums2[n_i]
                n_i -= 1
            insert_index -= 1

sol = Solution()
m = [1,2,3,0,0,0]
n = [2,5,6]
sol.merge(m, 3, n, 3)
print(m)

m = [1,2,3,0,0,0]
n = [4,5,6]
sol.merge(m, 3, n, 3)
print(m)

m = [4,5,6,0,0,0]
n = [1,2,3]
sol.merge(m, 3, n, 3)
print(m)

m = [4,5,6,0]
n = [1]
sol.merge(m, 3, n, 1)
print(m)

# [1,2,3,0,0,0], [2,5,6]
# [1,2,3,0,0,0], [4,5,6]
# [4,5,6,0,0,0], [1,2,3]
# [4,5,6,0], [1]

m = [2,0]
n = [1]
sol.merge(m, 1, n, 1)
print(m)

m = [1,0]
n = [2]
sol.merge(m, 1, n, 1)
print(m)

m = [0]
n = [1]
sol.merge(m, 0, n, 1)
print(m)

m = [1,0]
n = []
sol.merge(m, 1, n, 0)
print(m)
# [2,0], [1]
# [1,0], [2]

# [1,0], [4,5,6]
# [0], [1]
# [1], []
