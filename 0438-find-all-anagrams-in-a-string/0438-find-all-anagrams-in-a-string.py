from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m=len(s)
        n=len(p)
        start=0
        s1=Counter()
        p1=Counter(p)
        ans=[]
        for i in range(m):
            s1[s[i]]+=1
            if i>=n:
                s1[s[start]]-=1
                if s1[s[start]]==0:
                      del s1[s[start]]
                start+=1
            if s1==p1:
                ans.append(start)
                
            
        return ans
            
                    