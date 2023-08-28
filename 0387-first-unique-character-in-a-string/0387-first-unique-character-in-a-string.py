class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=i
            else:
                d[s[i]]=-1
        ans=10**9
        for i in d:
            if d[i]>=0:
                ans=min(ans,d[i])
        
        return -1 if ans==10**9 else  ans

        
        
