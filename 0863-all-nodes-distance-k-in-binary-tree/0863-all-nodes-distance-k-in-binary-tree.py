# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,parent):
            if node is None:
                return
            node.parent=parent
            node.done=False
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        
        q=collections.deque()
        q.append((target,0))
        target.done=True
        ans=[]

        while len(q)>0:
            node, d=q.popleft()
            if d==k:
                ans.append(node.val)
            print(node.left)
            for next_node in [node.left,node.right,node.parent]:
                if next_node !=None and  next_node.done!=True:
                    next_node.done=True
                    q.append((next_node,d+1))
                    
        return ans
                    
        
        
            