class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans,s,n=0,set(),len(nums)
        for i in nums: s.add(i)
        for i in range(n):
            if nums[i]-1 not in s:
                j=nums[i]
                while j in s:
                    j+=1
                ans=max(ans,j-nums[i])
        return ans

