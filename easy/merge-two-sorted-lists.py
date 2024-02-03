# Definition for singly-linked list.
import pdb
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2



sol = Solution()
a = ListNode(1, next=ListNode(2, next=ListNode(4, next=ListNode(5))))
b = ListNode(2, next=ListNode(3, next=ListNode(3)))
result = sol.mergeTwoLists(a, b)
pdb.set_trace()
                


        

