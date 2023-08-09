class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i=1
        minDiff=10**20
        
        while i<len(arr):
            if arr[i]-arr[i-1] <minDiff:
                ans=[]
                ans.append([arr[i-1],arr[i]])
                minDiff=arr[i]-arr[i-1]
            elif arr[i]-arr[i-1]==minDiff:
                ans.append([arr[i-1],arr[i]])
                minDiff=arr[i]-arr[i-1]
            i+=1
        return ans
                
                