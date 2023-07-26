class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        while l<r:
            mid=(l+r)//2
            curr=0
            need=1
            for w in weights:
                if w>mid:
                    break
                if curr+w>mid:
                    need+=1
                    curr=0
                curr+=w
            if need>days:
                l=mid+1
            else:
                r=mid
        return l