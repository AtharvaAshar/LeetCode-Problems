class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict={}
        for i,v in enumerate(nums):
            if v in dict and abs(dict[v]-i)<=k:
                return True
            dict[v]=i
        return False
        