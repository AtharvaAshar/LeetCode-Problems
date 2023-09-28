class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e,o=[],[]
        for i in nums:
            if i%2==1:
                o.append(i)
            else:
                e.append(i)
        e.extend(o)
        return e