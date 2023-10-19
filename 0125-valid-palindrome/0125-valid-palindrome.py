class Solution:
    def isPalindrome(self, s: str) -> bool:
        o=""
        for i in s:
            if i.isalnum():
                o+=i
        o=o.lower()
   
        def helper(s,si,ei):
            if si==ei or ei<0:
                return True
            if s[si]!=s[ei]:
                return False
            return helper(s,si+1,ei-1)
        return helper(o,0,len(o)-1) if len(o)>0 else True
    