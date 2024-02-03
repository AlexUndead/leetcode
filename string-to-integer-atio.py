# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        znak = ""
        result = ""
        _max = 2 ** 31 - 1
        _min = -2 ** 31
        trim_s = s.strip()
        if not trim_s:
            return 0
        znak = trim_s[0] if trim_s[0] in ("-", "+") else ""
        if znak:
            trim_s = trim_s[1:]

        for i in trim_s:
            if i.isnumeric():
                result += i
            else:
                break

        if result:
            if _min > int(znak + result):
                return _min
            elif _max < int(znak + result):
                return _max
            else:
                return int(znak + result)
        return 0
