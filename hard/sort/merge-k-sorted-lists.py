import pdb
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

#[[1,4,5],[1,3,4],[2,6]]
#pointes = {0: ListNode(1), 1: ListNode(1), 2: ListNode(2)}
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        _res = result = None
        pointers = {_list:lists[_list] for _list in range(len(lists)) if lists[_list]}

        while True:
            if not pointers:
                break
            _min = min(pointers, key=lambda x: pointers[x].val)
            if not result:
                _res = result = ListNode(val=pointers[_min].val)
            else:
                result.next = ListNode(val=pointers[_min].val)
                result = result.next

            if pointers[_min].next:
                pointers[_min] = pointers[_min].next
            else:
                del pointers[_min]

        return _res

lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
sol = Solution()
result = sol.mergeKLists(lists)
pdb.set_trace()
