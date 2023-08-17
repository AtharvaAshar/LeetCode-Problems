class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n=len(mat),len(mat[0])
        if mat[0][0]!=0:
            mat[0][0]=m+n
#             Travel Up
        for j in range(1,n):
            if mat[0][j]!=0:
                mat[0][j]= mat[0][j-1]+1
        for i in range(1,m):
            if mat[i][0]!=0:
                mat[i][0]=mat[i-1][0]+1
        for i in range(1,m):
            for j in range(1,n):
                if mat[i][j]!=0:
                    mat[i][j]=min(mat[i-1][j],mat[i][j-1]) + 1
        # Travel Down
        for j in range(n-2,-1,-1):
            if mat[m-1][j]!=0:
                mat[m-1][j]=min(mat[m-1][j],mat[m-1][j+1]+1)
        
        for i in range(m-2,-1,-1):
            if mat[i][n-1]!=0:
                mat[i][n-1]=min(mat[i][n-1],mat[i+1][n-1]+1)
        
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                if mat[i][j]!=0:
                    mat[i][j]=min(mat[i][j],min(mat[i+1][j],mat[i][j+1]) + 1)
        return mat
            
                    