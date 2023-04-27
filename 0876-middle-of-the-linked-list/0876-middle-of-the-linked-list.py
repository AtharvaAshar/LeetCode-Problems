# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            curr=curr.next
            count+=1
        if count%2!=0:
            middle=count//2 +1
            curr=head
            for i in range(middle-1):
                curr=curr.next
            return curr
        else:
            middle=count//2
            curr=head
            for i in range(middle):
                curr=curr.next
            return curr