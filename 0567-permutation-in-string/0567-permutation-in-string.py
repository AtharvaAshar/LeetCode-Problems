class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1=Counter(s1)
        c2=Counter()
        n,m=len(s1),len(s2)
        start=0
        
        for i in range(m):
            c2[s2[i]]+=1
            if i>=n:
                c2[s2[start]]-=1
                if c2[s2[start]]==0:
                    del c2[s2[start]]
                start+=1
            if c2==c1:
                return True
        return False