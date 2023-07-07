class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        left=0
        count=0
        best=0
        for right in range(n):
            if nums[right]!=1:
                count+=1
            while count>k:
                if nums[left]!=1:
                    count-=1
                left+=1
            best=max(best,right-left+1)
        return best