class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums,temp,ans):
            if len(nums)==0:
                ans.append(temp)
                return
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:],temp+[nums[i]],ans)
        ans=[]
        helper(nums,[],ans)
        return ans