class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        l,r=0,len(arr)
        while l<r:
            mid=(l+r)//2
            if arr[mid]>arr[mid+1]:
                r=mid
            elif arr[mid]<arr[mid+1]:
                l=mid+1
        return l
                