class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        for i in range(n):
            ans=max(ans,arr[i])
        return arr.index(ans)
                