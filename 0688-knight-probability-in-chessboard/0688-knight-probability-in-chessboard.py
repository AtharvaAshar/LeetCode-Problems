class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp=[[[0.0] * n for _ in range(n)] for _ in range(k + 1)]
        directions=[[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]
        dp[0][row][column]=1.0
        
        
        for m in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    for d in directions:
                        prevI=i-d[0]
                        prevJ=j-d[1]
                        if prevI>=0 and prevI<n and prevJ>=0 and prevJ<n:
                            dp[m][i][j]+=dp[m-1][prevI][prevJ]/8.0
        ans=0.0
        for i in range(n):
            for j in range(n):
                ans+=dp[k][i][j]
        return ans