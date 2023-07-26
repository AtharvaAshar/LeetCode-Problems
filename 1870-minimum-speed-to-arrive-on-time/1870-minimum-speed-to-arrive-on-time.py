class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def checkSpeed(speed,hour,dist):
            totalTime=0
            if speed==0: return False
            i=0
            while totalTime<=hour and i<len(dist)-1:
                totalTime+=math.ceil(dist[i]/speed)
                i+=1
            totalTime+=dist[-1]/speed
            return totalTime<=hour
        l,r=0,10**7
        ans=-1
        while l<=r:
            mid=(l+r)//2
            if checkSpeed(mid,hour,dist):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans