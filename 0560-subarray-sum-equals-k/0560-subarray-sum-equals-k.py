class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        total,c,n=0,0,len(nums)
        for i in range(n):
            total+=nums[i]
            if total-k in d:
                c+=d[total-k]

            if total not in d:
                d[total]=1
            else:
                d[total]+=1
        return c