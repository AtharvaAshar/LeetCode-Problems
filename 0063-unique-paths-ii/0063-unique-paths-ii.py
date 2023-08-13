class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=dict()
        def count(x,y):
            if obstacleGrid[x][y]==1:
                return 0
            
            if x==0 and y==0:
                return 1
            
            if (x,y) in dp.keys():
                return dp[(x,y)]
            path=0
            if x-1>=0:
                path+=count(x-1,y)
            if y-1>=0:
                path+=count(x,y-1)
            dp[(x,y)]=path
            return path
        return  count(r-1,c-1)