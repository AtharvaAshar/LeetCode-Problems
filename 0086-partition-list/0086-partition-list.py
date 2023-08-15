# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before=ListNode(0)
        after=ListNode(0)
        b_curr,a_curr=before,after
        curr=head
        while curr:
            if curr.val<x:
                b_curr.next,b_curr=curr,curr
            else:
                a_curr.next,a_curr=curr,curr
            curr=curr.next
        a_curr.next=None
        b_curr.next=after.next
        return before.next