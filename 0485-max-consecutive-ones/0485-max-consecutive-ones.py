class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        ans,curr=0,0
        for i in nums:
            if i==1:
                curr+=1
            else:
                ans=max(ans,curr)
                curr=0
        return max(curr,ans)