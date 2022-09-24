class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        space_str=' '
        a=[]
        start=0
        for i in spaces:
            a.append(s[start:i])
            start=i
        a.append(s[start:len(s)])
        return space_str.join(a)
                