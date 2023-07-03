# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(postorder) == 0:
            return None
        root = postorder[-1]
        root = TreeNode(root)
        i = inorder.index(root.val)
        leftInorder = inorder[:i]
        rightInorder = inorder[i+1:]
        leftPostorder = postorder[:len(leftInorder)]
        rightPostorder = postorder[len(leftInorder):-1]
        leftSubTree = self.buildTree(leftInorder, leftPostorder)
        rightSubTree = self.buildTree(rightInorder, rightPostorder)
        root.left = leftSubTree
        root.right = rightSubTree
        return root