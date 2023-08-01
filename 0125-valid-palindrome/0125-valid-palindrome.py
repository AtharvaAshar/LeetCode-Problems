class Solution:
    def isPalindrome(self, s: str) -> bool:
        o=''
        for i in s:
            if i.isalpha():
                o+=i.lower()
            elif i.isdigit():
                o+=i
        def checkP(si,ei,o):
            if si==ei or ei<0:
                return True
            
            if o[si]!=o[ei]:
                return False
            return checkP(si+1,ei-1,o)
        print(o)
        return checkP(0,len(o)-1,o) if len(o)>0 else True