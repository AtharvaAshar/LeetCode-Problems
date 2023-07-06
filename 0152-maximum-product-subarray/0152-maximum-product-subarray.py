class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        i=1
        prev_max,prev_min=nums[0],nums[0]
        ans=nums[0]
        while i < n:
            curr_max=max(prev_max*nums[i],prev_min*nums[i],nums[i])
            curr_min=min(prev_max*nums[i],prev_min*nums[i],nums[i])
            ans=max(ans,curr_max)
            prev_max=curr_max
            prev_min=curr_min
            i+=1
        return ans
            
        
            