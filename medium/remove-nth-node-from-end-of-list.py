# Definition for singly-linked list.
import pdb
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Решил за 3 часа. Правильный ответ пришел почти сразу. Долго писал код
# Решение имеет самое долгое время и кол-во памяти 
#(п.с. попробовал одно из самых залайканых решений время и память такие же как и у меня)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        pre_del_node = None
        cur_node = head
        if not cur_node.next:
            return cur_node.next

        while True:
            if not cur_node.next:
                pdb.set_trace()
                if n == 1:
                    pre_del_node.next = None
                    return head
                if count == n:
                    return head.next
                pre_del_node.next = pre_del_node.next.next
                return head

            if count > n and pre_del_node:
                pre_del_node = pre_del_node.next

            if not pre_del_node:
                pre_del_node = cur_node

            pre_node = cur_node
            cur_node = cur_node.next
            count += 1

a = ListNode(3, ListNode(4, ListNode(5, ListNode(6, None))))
#a = ListNode(1, ListNode(2, ListNode(3, None)))
sol = Solution()
#b = sol.removeNthFromEnd(a, 4)
#b = sol.removeNthFromEnd(a, 3)
#b = sol.removeNthFromEnd(a, 2)
b = sol.removeNthFromEnd(a, 1)

pdb.set_trace()
