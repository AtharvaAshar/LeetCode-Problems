# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr,l=head,0
        while(curr):
            curr,l=curr.next,l+1
        if l==n:
            return head.next
        curr=head
        for _ in range(1,l-n):
            curr=curr.next
        curr.next=curr.next.next
        return head