class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        curr=0
        prev=0
        ans=0
        for i in range(n):
            if nums[i]!=0:
                curr+=1
            else:
                ans=max(ans,prev+curr)
                prev=curr
                curr=0
        out=max(ans,prev+curr)
        return out-1 if out==n else out
            