class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        ans=0
        start=0
        for i in range(n):
            if i>0 and nums[i]<=nums[i-1]:
                start=i
            ans=max(ans,i-start+1)
        return ans