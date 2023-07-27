class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(batteries,time,n):
            return ((sum(min(i,time) for i in batteries))>=time*n)
        l,r=1,sum(batteries)/n
        while l<=r:
            time=(l+r)//2
            if not check(batteries,time,n):
                r=time-1
            else:
                l=time+1
        return int(l-1)
            