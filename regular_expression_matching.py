#Не решил
# мое недоделанное решение
#class Solution:
#    def create_plan(self, p: str) -> list:
#        plan = []
#        star = False
#        for symbol in p[::-1]:
#            if symbol == "*":
#                star = True
#            else:
#                plan.insert(0, (symbol, star))
#                if star:
#                    star = False
#
#        return plan
#
#
#    def isMatch(self, s: str, p: str) -> bool:
#        cursor = 0
#        is_match = False
#        star_podstrok = ""
#        plan = self.create_plan(p)
#        prev_symbol = ""
#        for symbol, star in plan:
#            if symbol == ".":
#                if star:
#                    is_match = True
#                    cursor = len(s)
#                    star_podstrok += s[cursor:len(s)]
#                else:
#                    try:
#                        if s[cursor]:
#                            is_match = True
#                            cursor += 1
#                    except IndexError:
#                        return False
#            else:
#                if star:
#                    try:
#                        while s[cursor] == symbol:
#                            is_match = True
#                            cursor += 1
#                            star_podstrok += s[cursor]
#                    except IndexError:
#                        continue
#                else:
#                    try:
#                        if symbol == s[cursor]:
#                            is_match = True
#                            cursor += 1
#                        else:
#                            return False
#                    except IndexError:
#                        return False
#
#            prev_symbol = symbol
#
#        if len(s) != cursor:
#            is_match = False
#
#        return is_match
class Solution(object):
    def isMatch(self, s, p):
        import pdb
        pdb.set_trace()
        # The DP table and the string s and p use the same indexes i and j, but
        # table[i][j] means the match status between p[:i] and s[:j], i.e.
        # table[0][0] means the match status of two empty strings, and
        # table[1][1] means the match status of p[0] and s[0]. Therefore, when
        # refering to the i-th and the j-th characters of p and s for updating
        # table[i][j], we use p[i - 1] and s[j - 1].

        # Initialize the table with False. The first row is satisfied.
        table = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]

        # Update the corner case of matching two empty strings.
        table[0][0] = True

        # Update the corner case of when s is an empty string but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous. [test_symbol_0]
        for i in range(2, len(p) + 1):
            table[i][0] = table[i - 2][0] and p[i - 1] == '*'

        for i in range(1, len(p) + 1):
            for j in range(1, len(s) + 1):
                if p[i - 1] != "*":
                    # Update the table by referring the diagonal element.
                    table[i][j] = table[i - 1][j - 1] and \
                                  (p[i - 1] == s[j - 1] or p[i - 1] == '.')
                else:
                    # Eliminations (referring to the vertical element)
                    # Either refer to the one before previous or the previous.
                    # I.e. * eliminate the previous or count the previous.
                    # [test_symbol_1]
                    table[i][j] = table[i - 2][j] or table[i - 1][j]

                    # Propagations (referring to the horizontal element)
                    # If p's previous one is equal to the current s, with
                    # helps of *, the status can be propagated from the left.
                    # [test_symbol_2]
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        table[i][j] |= table[i][j - 1]

        return table[-1][-1]


sol = Solution()
#sol.isMatch("aaa", "aaa*")
sol.isMatch("aaaab", "a*aab")
assert sol.isMatch("aa", "aa") == True
assert sol.isMatch("aa", "a") == False
assert sol.isMatch("a", "aa") == False
assert sol.isMatch("aa", "a.") == True
assert sol.isMatch("aaaa", "a.a.") == True
assert sol.isMatch("aaaa", ".a.a.") == False
assert sol.isMatch("b", ".*") == True
assert sol.isMatch("ab", ".*") == True
assert sol.isMatch("aaa", "a*") == True
assert sol.isMatch("aab", "c*a*b") == True
assert sol.isMatch("ab", ".*c") == False
assert sol.isMatch("aaa", "a*a") == True
assert sol.isMatch("aaaab", "a*aab") == True
assert sol.isMatch("aaa", "a*aaa") == True
assert sol.isMatch("aaab", "a*aaab") == True
assert sol.isMatch("caaab", "ca*aaab") == True
