# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        t = head
        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = 1 if val >= 10 else 0
            val %= 10
            t.next = ListNode(val) 
            t = t.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            t.next = ListNode((l1.val + carry) % 10)
            carry = 1 if l1.val == 9 and carry == 1 else 0
            l1 = l1.next
            t = t.next
        while l2:
            t.next = ListNode((l2.val + carry) % 10)
            carry = 1 if l2.val == 9 and carry == 1 else 0
            l2 = l2.next
            t = t.next
        if carry == 1:
            t.next = ListNode(1)
        return head.next
        