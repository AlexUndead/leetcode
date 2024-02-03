import pdb


def binary_search(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == val:
            return middle
        if nums[middle] < val:
            left = middle + 1
        elif nums[middle] > val:
            right = middle - 1

    return None

print(binary_search([4,6,12,44,124,492], 3))
