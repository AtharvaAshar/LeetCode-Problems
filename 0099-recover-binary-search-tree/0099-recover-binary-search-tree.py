# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root,res):
            if not root:
                return None
            inorder(root.left,res)
            res.append(root)
            inorder(root.right,res)
            return res
        res=inorder(root,[])
        for i in range(1,len(res)):
            if res[i].val<res[i-1].val:
                n1=res[i-1]
                break
        for i in range(len(res)-2,-1,-1):
            if res[i].val>res[i+1].val:
                n2=res[i+1]
                break
        n1.val,n2.val=n2.val,n1.val

        

       

            
            