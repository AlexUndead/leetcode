import pdb
from typing import Optional
from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_linked_list(nodes):
    cur = None
    head = None
    for node in nodes:
        if not head:
            head = ListNode(val=node)
            cur = head
            continue

        cur.next = ListNode(val=node)
        cur = cur.next

    return head


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = None
        new_head = None
        q = PriorityQueue()
        while head:
            q.put((head.val, head))
            head = head.next

        while q.empty() != True:
            _val, node = q.get()
            if not new_head:
                new_head = node
                cur = new_head
                continue
            cur.next = node
            cur = cur.next

        if cur:
            cur.next = None

        return new_head

sol = Solution()
#a = sol.sortList(ListNode(val=4, next=ListNode(val=2, next=ListNode(val=1, next=ListNode(val=3)))))
a = sol.sortList(get_linked_list([4,19,14,5,-3,1,8,5,11,15]))
pdb.set_trace()
