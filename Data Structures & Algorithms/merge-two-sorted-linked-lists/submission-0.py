# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        t = head
        while list1 and list2:
            val = -1
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else: 
                val = list2.val
                list2 = list2.next
            t.next = ListNode(val)
            t = t.next
        while list1:
            t.next = ListNode(list1.val)
            t = t.next
            list1 = list1.next
        while list2:
            t.next = ListNode(list2.val)
            t = t.next
            list2 = list2.next
        return head.next

        
        