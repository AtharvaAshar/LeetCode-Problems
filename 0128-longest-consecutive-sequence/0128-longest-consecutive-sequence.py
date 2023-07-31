class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet=set()
        n=len(nums)
        max_len=0
        for i in nums:
            hashSet.add(i)
        for i in range(n):
            if nums[i]-1 not in hashSet:
                j=nums[i]
                while j in hashSet:
                    j+=1
                max_len=max(max_len,j-nums[i])
        return max_len