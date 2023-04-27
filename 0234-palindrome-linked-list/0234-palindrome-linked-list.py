# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        isPalindrome=True
        curr=head
        while(curr):
            stack.append(curr.val)
            curr=curr.next
        curr=head
        while(curr):
            i=stack.pop()
            if i==curr.val:
                curr=curr.next
            else:
                isPalindrome=False
                break
        return isPalindrome