class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return i
        
                