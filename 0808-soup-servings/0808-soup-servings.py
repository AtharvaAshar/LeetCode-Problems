class Solution:
    def soupServings(self, n: int) -> float:
        def cal_dp(i,j):
            return (dp[max(0,i-4)][j] + dp[max(0,i-3)][j-1]+ dp[max(0,i-2)][max(0,j-2)] + dp[i-1][max(0,j-3)])/4
        dp={}
        dp[0]={0:0.5}
        m=ceil(n/25)
        for i in range(1,m+1):
            dp[0][i]=1
            dp[i]={0:0}
            for j in range(1,i+1):
                dp[j][i]=cal_dp(j,i)
                dp[i][j]=cal_dp(i,j)
            if dp[i][i]>1-1e-5:
                return 1
        return dp[m][m]
                