# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res=dummy
        dummy.next=head
        cur=head
        while cur and cur.next:
            if cur.val ==cur.next.val:
                dummy.next=cur.next
            else:
                dummy=dummy.next
            cur=cur.next
        return res.next


        