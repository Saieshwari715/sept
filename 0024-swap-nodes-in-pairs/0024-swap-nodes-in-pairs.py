# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        prev=dummy
        while head and head.next:
            first=head
            sec=head.next
            prev.next=sec
            first.next=sec.next
            sec.next=first
            prev=first
            head=first.next
        return dummy.next
