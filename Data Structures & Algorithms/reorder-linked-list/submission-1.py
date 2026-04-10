# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return None
        
        t = head
        elements = 1
        while t is not None:
            t = t.next
            elements += 1
        
        r = elements // 2


        t = head
        # go halfway
        for i in range(r):
            t = t.next

        r = t
        temp = ListNode()
        # reverse second half
        while t is not None:
            l = t.next
            t.next = temp.next
            temp.next = t
            t = l

        t = temp.next

        

        new_head = ListNode()
        new_list = new_head
        # combine lists
        while head != r:
            new_list.next = head
            head = head.next
            new_list = new_list.next
            if t is not None:
                new_list.next = t
                t = t.next
                new_list = new_list.next
            new_list.next = None
        head = new_head.next
        