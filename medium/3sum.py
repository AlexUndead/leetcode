#https://leetcode.com/problems/3sum/

import pdb
from typing import List

# Правильное решение (не принимает потому-что для него важен порядок добавлениея элементов)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #result = []
        #nums.sort()

        #max_index = len(nums) - 1
        #min_index_1 = 0
        #min_index_2 = 1

        #while True:
        #    prover = [nums[min_index_1], nums[min_index_2], nums[max_index]]
        #    if nums[min_index_1] == -82 and nums[max_index] == 65:
        #        pdb.set_trace()
        #    if nums[min_index_1] + nums[min_index_2] + nums[max_index] == 0 and [nums[min_index_1], nums[min_index_2], nums[max_index]] not in result:
        #        result.append([nums[min_index_1], nums[min_index_2], nums[max_index]])
        #    
        #    if min_index_1 == 0 and min_index_2 == 1 and max_index == 2:
        #        break

        #    if min_index_1 + 2 == max_index and min_index_2 + 1 == max_index:
        #        max_index -= 1
        #        min_index_1 = 0
        #        min_index_2 = 1
        #        continue

        #    if min_index_2 + 1 == max_index:
        #        min_index_1 += 1
        #        min_index_2 = min_index_1 + 1
        #        continue

        #    min_index_2 += 1

        #return result

        # Переписал на правильные индексы (не проходит по вромени)
        #result = []
        #nums.sort()
        #min_index = 0
        #max_index = len(nums) - 2
        #max_max_index = len(nums) - 1

        #while True:
        #    if nums[max_index] + nums[max_max_index] + nums[min_index] == 0 and [nums[min_index], nums[max_index], nums[max_max_index]] not in result:
        #        result.append([nums[min_index], nums[max_index], nums[max_max_index]])
        #    
        #    if min_index == len(nums) - 3 and max_index == len(nums) - 2 and max_max_index == len(nums) - 1:
        #        break

        #    if max_index - 1 == min_index and max_max_index - 2 == min_index:
        #        min_index += 1
        #        max_index = len(nums) - 2
        #        max_max_index = len(nums) - 1
        #        continue

        #    if max_index - 1 == min_index:
        #        max_max_index -= 1
        #        max_index = max_max_index - 1
        #        continue

        #    max_index -= 1

        result = []
        nums.sort()
        null = 0
        min_index = 1
        max_max_index = len(nums) - 1

        while True:
            #prov = [nums[null], nums[min_index], nums[max_max_index]]
            #if nums[null] == -2 and nums[max_max_index] == -1:
            #    pdb.set_trace()
            if nums[min_index] + nums[max_max_index] == nums[null] and [nums[null], nums[min_index], nums[max_max_index]] not in result:
                result.append([nums[null], nums[min_index], nums[max_max_index]])

            if null == 0 and min_index == 1 and max_max_index == 2:
                break
            
            if null + 2 == max_max_index and min_index + 1 == max_max_index or nums[null] + nums[min_index] > nums[max_max_index]:
                max_max_index -= 1
                null = 0
                min_index = null + 1
                continue

            if min_index + 1 == max_max_index:
                null += 1
                min_index = null + 1
                continue


            if nums[null] > nums[min_index] + nums[max_max_index]:
                null += 1
                min_index = null + 1
                continue
            min_index += 1

        return result


sol = Solution()
print(sol.threeSum([-5,0,-2,3,-2,1,1,3,0,-5,3,3,0,-1]))
assert sol.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
assert sol.threeSum([0,1,1]) == []
assert sol.threeSum([0,0,0]) == [[0,0,0]]
assert sol.threeSum([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76, 26,15,-29,36,-29,10,-70,69,17,49]) == [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],[-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],[-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],[-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],[-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],[-29,-14,43],[-29,1,28],[-29,12,17],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]
