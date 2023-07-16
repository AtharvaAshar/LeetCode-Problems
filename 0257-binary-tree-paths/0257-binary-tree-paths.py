# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return []
        q=[(root,str(root.val))]
        res=[]
        while q:
            curr,s=q.pop(0)
            if not curr.left and not curr.right:
                res.append(s)
            if curr.left:
                q.append((curr.left,s+"->"+str(curr.left.val)))
            if curr.right:
                q.append((curr.right,s+"->"+str(curr.right.val)))
        return res