class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        dp, ans = [10**10] * (len(obstacles) + 1), []
        for elem in obstacles:
            ind = bisect.bisect(dp, elem)
            ans += [ind + 1]
            dp[ind] = elem  
        return ans