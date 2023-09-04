# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow,fast=head,head
            while True:
                slow,fast=slow.next,fast.next.next
                if slow==fast:
                    break
            print(slow.val)
            while head!=slow:
                head,slow=head.next,slow.next
            return head
        except:
            return None
