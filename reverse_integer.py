#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        _max = 2 ** 31 - 1
        negative = x < 0
        list_x = list(str(x))
        if negative:
            list_x.pop(0)
        count = len(list_x)
        list_max = list(str(_max))
        list_min = list(str(_max + 1))
        need_check = count == len(list_max)
        result = ""

        if count > len(list_max):
            return 0

        for i in range(count):
            if need_check:
                if negative:
                    if list_x[-1] > list_min[i]:
                        return 0
                    elif list_x[-1] < list_min[i]:
                        need_check = False
                else:
                    if list_x[-1] > list_max[i]:
                        return 0
                    elif list_x[-1] > list_max[i]:
                        need_check = False
            result += list_x[-1]
            list_x.pop()

        if negative:
            result = "-" + result

        return int(result)
