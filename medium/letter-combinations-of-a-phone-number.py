#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
import pdb
from typing import List


# Решал в лоб, очень сложный код с кучей счетчиков, плохо по скорости, плохо по памяти, сложно читать
# задача на бектрекинг
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result_mumnoj = len(mapping[digits[0]])
        for i in digits[1:]:
            result_mumnoj *= len(mapping[i])

        results = result_mumnoj * [""]

        koef = []
        asdf = 1
        for i in digits[::-1]:
            koef.insert(0, asdf)
            asdf *= len(mapping[i])

        cursors = [0 for i in range(len(digits))]

        _koef = koef[::1]
        for ccc, result in enumerate(results):
            if _koef == [16, 5, 1, 1]:
                pdb.set_trace()
            for c, dig in enumerate(digits):
                results[ccc] += mapping[dig][cursors[c]]

            for c_koef, i in enumerate(_koef):
                _koef[c_koef] -= 1
                if _koef[c_koef] == 0:
                    cursors[c_koef] += 1
                    if cursors[c_koef] == len(mapping[digits[c_koef]]):
                        cursors[c_koef] = 0
                    _koef[c_koef] = koef[c_koef]

        return results

sol = Solution()
print(sol.letterCombinations("5678"))
assert sol.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
assert sol.letterCombinations("2") == ["a","b","c"]
assert sol.letterCombinations("") == []
