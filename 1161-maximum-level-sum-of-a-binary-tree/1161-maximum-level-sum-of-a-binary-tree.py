# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        level=0
        q.append(root)
        maxSum=-10**6
        ansLevel=0
        while q:
            level+=1
            lsum=0
            for _ in range(len(q)):
                curr=q.popleft()
                lsum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if maxSum<lsum:
                maxSum,ansLevel=lsum,level
                
        return ansLevel
            