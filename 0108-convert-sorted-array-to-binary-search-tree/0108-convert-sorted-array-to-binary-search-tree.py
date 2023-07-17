# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums)==0:
            return
        root=ListNode(nums[len(nums)//2])
        l=self.sortedArrayToBST(nums[:len(nums)//2])
        r=self.sortedArrayToBST(nums[len(nums)//2+1:])
        root.left=l
        root.right=r
        return root