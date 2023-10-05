class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c,n=0,0
        for num in nums:
            if c==0:
                n=num
                c+=1
            elif num==n:
                c+=1
            else:
                c-=1
        return n