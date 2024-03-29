# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q,ans= deque(),[]
        q.append(root)
        if not root:
            return []
        while q:
            l=[]
            for i in range(len(q)):
                curr=q.popleft()
                l.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(l)
        return ans[::-1]