class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def score(dp,l,r,nums):
            if dp[l][r]!=-1: 
                return dp[l][r]
            if l==r:
                return nums[l]
            left=nums[l]-score(dp,l+1,r,nums)
            right=nums[r]-score(dp,l,r-1,nums)
            dp[l][r]=max(left,right)
            return dp[l][r]
        n=len(nums)
        dp=[[-1 for _ in range(n)]for _ in range(n)] 
        return score(dp,0,n-1,nums)>=0