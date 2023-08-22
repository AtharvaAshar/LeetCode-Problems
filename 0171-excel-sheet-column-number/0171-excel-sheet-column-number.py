class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        for digit in columnTitle:
            res=res*26 + ord(digit) -ord("A") + 1
        return res
        