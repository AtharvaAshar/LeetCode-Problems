# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0: return None
        root=preorder[0]
        i=inorder.index(root)
        root=TreeNode(root)
        leftInorder=inorder[:i]
        rightInorder=inorder[i+1:]
        leftPreorder=preorder[1:len(leftInorder)+1]
        rightPreorder=preorder[len(leftInorder)+1:]
        leftSubtree=self.buildTree(leftPreorder,leftInorder)
        rightSubtree=self.buildTree(rightPreorder,rightInorder)
        root.left=leftSubtree
        root.right=rightSubtree
        return root
        
        