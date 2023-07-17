# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkBST2(root):
            if root == None:
                return 10**20, -10**20, True
            leftMin, leftMax, isLeftBST,  = checkBST2(root.left)
            rightMin, rightMax, isRightBST = checkBST2(root.right)
            minimum = min(root.val, leftMin, rightMin)
            maximum = max(root.val, leftMax, rightMax)
            isTreeBST = True
            if root.val <= leftMax or root.val >= rightMin:
                isTreeBST = False
            if not (isLeftBST) or not (isRightBST):
                isTreeBST = False

            return  minimum, maximum,isTreeBST
        _,_,output=checkBST2(root)
        return output
            