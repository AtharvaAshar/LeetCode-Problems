# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start,end):
            variations=[]
            if start>end:
                variations.append(None)
                return variations
            if (start,end) in dp:
                return dp[(start,end)]
            for i in range(start,end+1):
                left=helper(start,i-1)
                right=helper(i+1,end)
                for l in left:
                    for r in right:
                        root=TreeNode(i,l,r)
                        
                        variations.append(root)
            dp[(start,end)]=variations
            return variations
        dp={}
        return helper(1,n)