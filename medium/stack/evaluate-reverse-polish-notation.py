from queue import LifoQueue
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = LifoQueue()
        operations = {
            "+": lambda x,y: x+y,
            "-": lambda x,y: x-y,
            "*": lambda x,y: x*y,
            "/": lambda x,y: x/y,
        }

        for token in tokens:
            if token in operations:
                _y = int(queue.get())
                _x = int(queue.get())
                queue.put(operations[token](_x, _y))
            else:
                queue.put(token)

        return int(queue.get())

sol = Solution()
print(sol.evalRPN(["18"]))
print(sol.evalRPN(["2","1","+","3","*"]))
print(sol.evalRPN(["4","13","5","/","+"]))
print(sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+", "5","+"]))
