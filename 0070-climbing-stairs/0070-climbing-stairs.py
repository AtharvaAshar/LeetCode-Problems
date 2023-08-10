class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        oneStepback=2
        twoStepback=1
        ans=0
        for _ in range(2,n):
            ans=oneStepback+twoStepback
            twoStepback=oneStepback
            oneStepback=ans
        return ans