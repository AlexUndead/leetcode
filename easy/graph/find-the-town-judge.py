import pdb
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        pred_judegs = {judge: {"out" : set(), "in": set()} for judge in range(1, n+1)}

        for out, _in in trust:
            pred_judegs[out]["out"].add(_in)
            pred_judegs[_in]["in"].add(out)

        without_in = list(filter(lambda x: not pred_judegs[x]["out"] and len(pred_judegs[x]["in"]) == n - 1, pred_judegs))
        if not without_in:
            return -1
        return without_in[0]

sol = Solution()
assert sol.findJudge(n=1, trust=[]) == 1
assert sol.findJudge(n=2, trust=[]) == -1
assert sol.findJudge(n=2, trust=[[1,2]]) == 2
assert sol.findJudge(n=3, trust=[[1,3], [2,3]]) == 3
assert sol.findJudge(n=3, trust=[[1,2], [2,3]]) == -1
assert sol.findJudge(n=4, trust=[[1,2], [3,2]]) == -1
assert sol.findJudge(n=4, trust=[[1,2], [2,3], [3,4], [4,1]]) == -1
assert sol.findJudge(n=4, trust=[[1,2], [3,2], [3,4], [1,4]]) == -1
