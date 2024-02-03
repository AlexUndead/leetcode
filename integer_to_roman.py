class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        structure = (
            ("I", "IV", "V", "IX"),
            ("X", "XL", "L", "XC"),
            ("C", "CD", "D", "CM"),
            ("M"),
        )
        for k, number in enumerate(str(num)[::-1]):
            pred_result = ""
            number = int(number)
            if number < 4:
                i = 1
                while i <= number:
                    pred_result += structure[k][0]
                    i += 1
            elif number == 4:
                pred_result += structure[k][1]
            elif number == 5:
                pred_result += structure[k][2]
            elif number > 5 and number < 9:
                svg = structure[k][2]
                i = 6
                while i <= number:
                    svg += structure[k][0]
                    i += 1
                pred_result += svg
            elif number == 9:
                pred_result = structure[k][3]

            result = pred_result + result

        return result

sol = Solution()
sol.intToRoman(1994)
assert sol.intToRoman(1) == "I"
assert sol.intToRoman(2) == "II"
assert sol.intToRoman(3) == "III"
assert sol.intToRoman(4) == "IV"
assert sol.intToRoman(5) == "V"
assert sol.intToRoman(6) == "VI"
assert sol.intToRoman(7) == "VII"
assert sol.intToRoman(8) == "VIII"
assert sol.intToRoman(9) == "IX"
assert sol.intToRoman(58) == "LVIII"
assert sol.intToRoman(1994) == "MCMXCIV"
