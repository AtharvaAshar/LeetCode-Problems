class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans,w_sum=-10**20,0
        start=0
        for i in range(len(nums)):
            w_sum+=nums[i]
            if i-start+1==k:
                ans=max(ans,w_sum/k)
                w_sum-=nums[start]
                start+=1
                
        return ans