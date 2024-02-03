# Ебанутое задание
# https://leetcode.com/problems/zigzag-conversion/description/

class Solution:
    def vert(self, strings):
        string = strings.pop(0)
        strings = strings.append(string)

    def sk_vert(self, strings, count_s, numRows):
        while count_s % numRows != 0:
            self.vert(strings)
            count_s += 1

        return strings

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        elif numRows == 2:
            first = ""
            second = ""

            for i in range(len(s)):
                if i == 0:
                    first += s[i]
                    continue
                if i % 2 == 0:
                    first += s[i]
                else:
                    second += s[i]

            return first + second

        else:
            s_list = [sym for sym in s]
            strings = ["" for _ in range(numRows)]
            cycle = False
            norm_cycl = numRows
            ne_cycle = numRows - 2
            asdf = -1
            ffff = 0

            for i in range(len(s_list)):
                if cycle:
                    asdf -= 1
                    if ne_cycle == 1:
                        cycle = False
                        ne_cycle = numRows - 1
                        norm_cycl = numRows
                    ne_cycle -= 1
                    strings[asdf] += s_list[i]
                    if ne_cycle == numRows - 2:
                        asdf = -1
                    continue

                ffff += 1
                if i != 0 and norm_cycl == 1:
                    cycle = True

                string = strings.pop(0)
                string += s_list[i]
                strings.append(string)
                norm_cycl -= 1
            pre_strings = self.sk_vert(strings, ffff, numRows)
            fin = ""
            for i in pre_strings:
                fin += i

            return fin


# Решение Егора
#class Solution(object):
#    def calc(self, k):
#        num = k
#        while num <= self.s_len or num - 2*k <= self.s_len:
#            if num - 2*k > 0:
#                yield num - 2*k
#            yield num
#            if self.num_rows > 1:
#                num += 2 * (self.num_rows - 1)
#            else:
#                num += 1
#
#    def convert(self, s, numRows):
#        self.num_rows = numRows
#        self.s_len = len(s)
#        ans = ""
#        for i in range(self.num_rows):
#            indexes = set(self.calc(i))
#            ans += "".join(s[i] for i in range(self.s_len) if i in indexes)
#        return ans
