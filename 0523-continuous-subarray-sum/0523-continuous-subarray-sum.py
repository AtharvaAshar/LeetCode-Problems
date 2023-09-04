class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        total,n=0,len(nums)
        for i in range(n):
            total+=nums[i]
            if total%k in d  and i-d[total%k]>=2:
                return True
            if total%k not in d:
                d[total%k]=i
        return False
        