class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        d={}
        count = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if i+k in d:
                count+=d[i]*d[i+k]

        return count