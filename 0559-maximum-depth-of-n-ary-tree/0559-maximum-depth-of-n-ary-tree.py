"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return 0 if root is None else 1 if not root.children else 1 + max(0, *(self.maxDepth(child) for child in root.children))