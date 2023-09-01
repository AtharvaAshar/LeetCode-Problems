class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1): 
            count=0
            a=i
            while a:
                count+=a & 1
                a>>=1
            res.append(count)
        return res