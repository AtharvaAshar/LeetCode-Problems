# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        node=ListNode(-1)
        node.next=head
        current=node
        while current.next!=None:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return node.next
    