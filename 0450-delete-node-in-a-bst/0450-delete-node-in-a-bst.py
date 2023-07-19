# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minimum(root):
            if root is None:
                return 10**20
            if root.left is None:
                return root.val
            return minimum(root.left)
        if root is None: 
            return None
        if root.val > key:
            root.left=self.deleteNode(root.left,key)
            return root
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
            return root
        else:
            if root.left ==None and root.right==None:
                return None
            elif root.left==None and root.right is not None:
                return root.right
            elif root.left!=None and root.right is  None:
                return root.left
            else:
                replacement=minimum(root.right)
                root.val=replacement
                newRight=self.deleteNode(root.right,replacement)
                root.right=newRight
                return root
                