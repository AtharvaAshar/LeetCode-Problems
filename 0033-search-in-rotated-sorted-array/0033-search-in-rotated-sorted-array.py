class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        def good(x):
            if nums[0]<=target<=nums[x]:
                return True
            if nums[x]<nums[0]:
                return target>=nums[0] or target<=nums[x]
            return False
        while left<right:
            mid=(left+right)//2
            if good(mid):
                right=mid
            else:
                left=mid+1
        return left if nums[left]==target else -1