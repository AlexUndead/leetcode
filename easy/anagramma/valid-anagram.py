import pdb


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        syms = {}
        for i in s:
            if i in syms:
                syms[i] += 1
            else:
                syms[i] = 1

        for i in t:
            if i not in syms:
                return False
            else:
                if syms[i] > 1:
                    syms[i] -= 1
                else:
                    del syms[i]

        return not bool(syms)



sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))
print(sol.isAnagram("rat", "car"))

