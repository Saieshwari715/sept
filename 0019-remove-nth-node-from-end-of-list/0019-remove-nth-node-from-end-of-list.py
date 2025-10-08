# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy=ListNode()
        res=dummy
        dummy.next=head
        cur=head
        for i in range(n):
            cur=cur.next
        while cur:
            cur=cur.next
            dummy=dummy.next
        dummy.next=dummy.next.next
        return res.next


        