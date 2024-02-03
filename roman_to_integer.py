#https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        #Медленное решение
        #result = 0
        #structure = {
        #    "M": 1000,
        #    "D": 500,
        #    "C": 100,
        #    "L": 50,
        #    "X": 10,
        #    "V": 5,
        #    "I": 1,
        #}
        #pre = ""
        #for i in s:
        #    if pre and structure[pre] < structure[i]:
        #        result -= structure[pre] * 2
        #    result += structure[i]
        #    pre = i

        #return result
        result = 0
        structure = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }
        pre = ""
        for i in s:
            if pre and structure[pre] < structure[i]:
                result -= structure[pre] * 2
            result += structure[i]
            pre = i

        return result


sol = Solution()
print(sol.romanToInt("MCMXCIV"))
assert sol.romanToInt("III") == 3
assert sol.romanToInt("LVIII") == 58
assert sol.romanToInt("MCMXCIV") == 1994
