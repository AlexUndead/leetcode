from queue import LifoQueue
from collections import defaultdict
from typing import List


class Solution:
    operations = {
        "+": lambda x,y: x+y,
        "-": lambda x,y: x-y,
        "*": lambda x,y: x*y,
        "/": lambda x,y: x/y,
    }

    def multi_operation(self, values: List[str], operation: str) -> int:
        if not values:
            return None

        result = int(values[0])
        for value in values[1:]:
            int_value = int(value)
            result = self.operations[operation](result, int_value)

        return result

    def polis_notation(self, tokens: str) -> int:
        queue = LifoQueue()

        for token in tokens:
            if token in (" ", "("):
                continue
            if token in self.operations:
                operations = defaultdict(list)
                operations["operator"] = token
                queue.put(operations)
            elif token == ")":
                operation = queue.get()
                result = self.multi_operation(
                    operation["values"], operation["operator"]
                )
                if not queue.empty():
                    operation = queue.get()
                    operation["values"].append(result)
                    queue.put(operation)
                else:
                    return result if result else 0
            else:
                operation = queue.get()
                operation["values"].append(token)
                queue.put(operation)




sol = Solution()
print(sol.polis_notation("(+ 2 4)"))
print(sol.polis_notation("(*(+3 6)(*1 2 3))"))
