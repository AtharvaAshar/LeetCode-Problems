# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        q=[(root,root.val,[root.val])]
        res=[]
        
        while q:
            curr,val,l=q.pop(0)
            if not curr.left and not curr.right and val==targetSum:
                res.append(l)
            if curr.left:
                q.append((curr.left,val+curr.left.val,l+[curr.left.val]))
            if curr.right:
                q.append((curr.right,val+curr.right.val,l+[curr.right.val]))
        return res