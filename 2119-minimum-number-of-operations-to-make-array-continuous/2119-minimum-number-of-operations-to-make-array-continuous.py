class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ans=n
        hash_set=set()
        for x in nums:
            hash_set.add(x)
        unique=sorted(list(hash_set))
        j=0
        for i in range(len(unique)):
            while j<len(unique) and unique[j]<unique[i]+n:
                j+=1
            ans=min(ans,n-j+i)
        return ans



        
            