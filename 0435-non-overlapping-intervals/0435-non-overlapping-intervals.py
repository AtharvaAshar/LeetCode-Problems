class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals=sorted(intervals,key=lambda x: x[1])
        ans,endtime=0,-60000
        for i in range(len(intervals)):
            if intervals[i][0]<endtime:
                ans+=1
            else:
                endtime=intervals[i][1]
        return ans