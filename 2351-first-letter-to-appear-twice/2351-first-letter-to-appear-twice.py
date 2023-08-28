class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                return s[i]
            
            
        