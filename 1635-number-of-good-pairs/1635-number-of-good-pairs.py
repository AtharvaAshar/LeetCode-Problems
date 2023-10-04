class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            for j in range(i,n):
                if  nums[i]==nums[j] and i<j:
                    c+=1
        return c