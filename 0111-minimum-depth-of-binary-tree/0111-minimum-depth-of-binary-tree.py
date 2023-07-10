# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def minDepth(self, root: Optional[TreeNode]) -> int:
        from queue import Queue
        q=Queue()
        q.put(root)
        d=1
        if root is None:
            return 0
        while not(q.empty()):
            for i in range(q.qsize()):
                curr=q.get()
                if curr.left is not None:
                    q.put(curr.left)
                if curr.right is not None:
                    q.put(curr.right)
                if curr.left is None and curr.right is None:
                    return d
            d+=1
                
        return d