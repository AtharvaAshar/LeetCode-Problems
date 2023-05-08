class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n,total=len(mat),0
        for i in range(n):
            total+=mat[i][i] + mat[i][n-1-i]
            
        if n%2!=0:
            total-=mat[n//2][n//2]
        return total