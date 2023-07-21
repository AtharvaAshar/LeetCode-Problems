class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        if not nums: return 0
        n=len(nums)
        dp=[1]*n
        count=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i]> nums[j]:
                    if dp[j]+1>dp[i]:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]
                        
        longest_len=max(dp)
        
        return sum(x for index ,x in enumerate(count) if dp[index]==longest_len)