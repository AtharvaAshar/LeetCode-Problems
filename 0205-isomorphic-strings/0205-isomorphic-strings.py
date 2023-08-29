class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1=defaultdict(list)       
        s2=defaultdict(list)
        for i in range(len(s)):
            s1[s[i]].append(i)
            s2[t[i]].append(i)
            
        
        return list(s1.values())==list(s2.values())
            
        