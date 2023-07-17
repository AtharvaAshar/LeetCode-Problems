# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def createTree(a):
            if len(a)==0:
                return
            root=ListNode(a[len(a)//2])
            l=createTree(a[:len(a)//2])
            r=createTree(a[len(a)//2+1:])
            root.left=l
            root.right=r
            return root
        if head is []:
            return head
        l=[]
        while head:
            l.append(head.val)
            head=head.next
        return createTree(l)