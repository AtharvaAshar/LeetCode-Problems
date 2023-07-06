class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        window=0
        ans=n+1
        start=0
        for i in range(n):
            window+=nums[i]
            while window>=target:
                ans=min(ans,i-start+1)
                window-=nums[start]
                start+=1
                
        return 0 if ans==n+1 else ans