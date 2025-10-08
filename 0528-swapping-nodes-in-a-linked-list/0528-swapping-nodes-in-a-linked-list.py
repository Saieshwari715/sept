# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        res=dummy
        for i in range(k):
            dummy=dummy.next
        first=dummy
        cur=res
        while dummy:
            cur=cur.next
            dummy=dummy.next
        second=cur
        first.val,second.val=second.val,first.val
        return res.next



        