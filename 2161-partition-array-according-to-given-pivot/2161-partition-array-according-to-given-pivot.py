class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n=len(nums)
        l=[]
        g=[]
        e=[]
        for i in range(n):
            if nums[i]<pivot:
                l.append(nums[i])
            elif nums[i]==pivot:
                e.append(nums[i])
            else:
                g.append(nums[i])
        return l + e+ g