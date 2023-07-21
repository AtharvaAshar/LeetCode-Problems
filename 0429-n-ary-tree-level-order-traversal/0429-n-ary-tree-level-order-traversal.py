"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q,ans= deque(),[]
        q.append(root)
        if not root:
            return []
        while q:
            l=[]
            for i in range(len(q)):
                curr=q.popleft()
                if curr is not None:
                    l.append(curr.val)
                    for child in curr.children:
                        q.append(child)
            ans.append(l)
            
        return ans
                