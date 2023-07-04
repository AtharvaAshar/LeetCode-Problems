class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #XOR of same number is zero
        xor=0
        for i in nums:
            xor=xor^i
        return xor
        