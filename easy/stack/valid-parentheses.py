from queue import LifoQueue


class Solution():
    def isValid(self, s):
        queue = LifoQueue()
        skobs = {"}": "{", ")": "(", "]": "["}

        for i in s:
            if i not in skobs:
                queue.put(i)
            else:
                if queue.empty():
                    return False

                skob = queue.get()
                if skobs[i] != skob:
                    return False

        return queue.empty()


sol = Solution()
assert sol.isValid("]") == False
assert sol.isValid("[") == False
assert sol.isValid("([]{])") == False
assert sol.isValid("()[]{]") == False
assert sol.isValid("()") == True
assert sol.isValid("()[]{}") == True
assert sol.isValid("(]") == False
