class Solution:
    def romanToInt(self, s: str) -> int:
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=list(s)
        i=len(s)-1
        integer=0
        while(i!=-1):
            if((d[l[i-1]]<d[l[i]]) and i!=0):
                integer+=d[l[i]]-d[l[i-1]]
                i-=2
            else:
                integer+=d[l[i]]
                i-=1
        return integer