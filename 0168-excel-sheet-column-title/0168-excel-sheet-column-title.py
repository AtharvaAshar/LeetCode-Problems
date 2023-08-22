class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=''
        while columnNumber>0:
            s+=chr((columnNumber-1)%26 + ord("A"))
            columnNumber=(columnNumber-1)//26
        return s[::-1]