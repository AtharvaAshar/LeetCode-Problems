class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum=0
        i=0
        while i!=len(nums):
            sum+=min(nums[i],nums[i+1])
            i+=2
        return sum
        
            