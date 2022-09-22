class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n= len(nums)
        dict={}
        for i in range(n):
            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                return True
        return False