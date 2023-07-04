class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums)==2: return [nums[0],nums[1]]
        nums.sort()
        output=set()
        if nums[0]!=nums[1]:
            output.add(nums[0])
        if nums[-1]!=nums[-2]:
            output.add(nums[-1])
        i=0
        while i < len(nums)-1:
            if nums[i]!=nums[i+1]:
                output.add(nums[i])
                i+=1
            else: i+=2
        return list(output)