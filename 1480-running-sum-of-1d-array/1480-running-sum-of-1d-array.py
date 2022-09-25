class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output=[]
        tempsum=0
        for i in range(len(nums)):
            if i==0:
                output.append(nums[i])
            else:
                output.append(output[i-1]+nums[i])
        return output
        