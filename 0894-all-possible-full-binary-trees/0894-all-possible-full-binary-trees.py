# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def constructTree(x):
            if x==1:
                return [TreeNode()]
            res=[]
            for left in range(x):
                right=x-left-1
                
                left_trees=constructTree(left)
                right_trees=constructTree(right)
                
                for i in left_trees:
                    for j in right_trees:
                        res.append(TreeNode(0,i,j))
            return res
        if n%2==0: 
            return []
        return constructTree(n)