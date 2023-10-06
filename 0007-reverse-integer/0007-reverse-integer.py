class Solution:
    def reverse(self, x: int) -> int:
        res=0
        og=x
        x=abs(x)
        while x>0:
            r=x%10
            res=res*10 + r
            x=x//10
        if res < 2**31:
            return -res if og<0 else res
        return 0