# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while(curr):
            if curr.next is None or curr.next.val!=curr.val:
                curr=curr.next
            else:
                curr.next=curr.next.next
        return head