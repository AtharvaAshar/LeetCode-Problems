class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def isIncreasing(nums):
            for x , y in zip(nums,nums[1:]):
                if x>y:
                    return False
            return True
        
        return isIncreasing(nums) or isIncreasing(list(reversed(nums)))