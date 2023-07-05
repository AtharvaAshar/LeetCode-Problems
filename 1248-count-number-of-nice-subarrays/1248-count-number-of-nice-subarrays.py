class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prevSum=[0]*(n+1)
        odd=0
        ans=0
        for i in range(n):
            prevSum[odd]+=1
            
            if nums[i]%2!=0: odd+=1
            if odd>=k: 
                ans+=prevSum[odd-k]
            
                
            
        return ans