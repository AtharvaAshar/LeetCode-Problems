# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def minAndMax(root):
            if root is None:
                return 10**20,-10 **20
            lmin,lmax=minAndMax(root.left)
            rmin,rmax=minAndMax(root.right)

            return [min(root.val,min(lmin,rmin)),max(root.val,max(lmax,rmax))]
        if root is None:
            return True
        leftMax=minAndMax(root.left)[1]
        rightMin=minAndMax(root.right)[0]
        if root.val>=rightMin or root.val<=leftMax:
            return False
        
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        
            