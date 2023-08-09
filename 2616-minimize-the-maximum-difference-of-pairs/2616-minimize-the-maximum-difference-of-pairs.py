class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l,r=0,nums[-1]-nums[0]
        def check(diff,p):
            count,i=0,1
            while i<len(nums):
                if nums[i]-nums[i-1]<=diff:
                    i+=1
                    count+=1
                i+=1
            return count 
        while l<r:
            mid=(l+r)//2
            if check(mid,p)>=p:
                r=mid
            else:
                l=mid+1
        return l
                