class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d={}
        count = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i]>1 and k==0:
                count+=1
            elif i+k in d and k!=0:
                count+=1
                d[i]=0
            
        return count