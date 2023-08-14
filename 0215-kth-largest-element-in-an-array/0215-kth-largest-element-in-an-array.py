class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        pivot=random.choice(nums)
        greaterThanPivot=[x for x in nums if x>pivot]
        equalToPivot=[x for x in nums if x==pivot]
        lessThanPivot=[x for x in nums if x<pivot]
         
        l1,l2=len(greaterThanPivot),len(equalToPivot)
        if k<=l1:
            return self.findKthLargest(greaterThanPivot,k)
        elif k>l1+l2:
            return self.findKthLargest(lessThanPivot,k-l1-l2)
        else:
            return equalToPivot[0]
                