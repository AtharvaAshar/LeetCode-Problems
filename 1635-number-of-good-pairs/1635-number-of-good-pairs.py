class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d={} 
        c=0
        for i in nums:
            if i not in d:
                d.setdefault(i,1)
            else:
                c+=d[i]
                d[i]+=1
        return c