class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        c=collections.Counter()
        for x in arr:
            if x-difference in c:
                c[x]=max(c[x-difference]+1,c[x])
            else:
                c[x]=1
        return max(c.values())
        
            