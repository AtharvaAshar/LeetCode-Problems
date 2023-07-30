class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count=0
        n=len(nums)
        c=len(set(nums))
        for i in range(n):
            s=set()
            for j in range(i,n):
                s.add(nums[j])
                if len(s)==c:
                    count+=1
                elif len(s)>c:
                    break
        return count