import pdb


# Решил быстро, долго выполняется, много памяти занимает
# Попробовал самое залайканное решение, статистика такая-же плохая как и у меня
class Solution:
    def isValid(self, s: str) -> bool:
        deq = []
        _open = ("(", "[", "{")
        close = (")", "]", "}")

        for i in s:
            if i in _open:
                deq.append(i)

            if i in close:
                if not deq:
                    return False

                k = deq.pop() 
                for c, j in enumerate(_open): 
                    if k == j and i != close[c]:
                        return False
        
        if len(deq) > 0:
            return False
        return True


sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))

