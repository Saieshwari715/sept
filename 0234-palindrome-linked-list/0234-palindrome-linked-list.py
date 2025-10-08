# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s=[]
        cur=head
        while cur:
            s.append(cur.val)
            cur=cur.next
        cur=head
        while cur and cur.val==s.pop():
            cur=cur.next
        return cur is None