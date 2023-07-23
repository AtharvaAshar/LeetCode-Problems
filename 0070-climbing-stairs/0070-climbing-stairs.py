class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 0
        if n==1: return n
        if n==2: return 2
        oneStepback=2
        twoStepback=1
        ans=0
        for _ in range(2,n):
            ans=oneStepback+twoStepback
            twoStepback=oneStepback
            oneStepback=ans
        return ans