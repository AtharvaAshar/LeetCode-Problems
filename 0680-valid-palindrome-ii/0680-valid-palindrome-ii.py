class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkP(s,si,ei):
            if si==ei or ei<0:
                return True
            if s[si]!=s[ei]:
                return False
            return checkP(s,si+1,ei-1)
        
        
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                delete_i=s[i+1:j+1]
                delete_j=s[i:j]
                return checkP(delete_i,0,len(delete_i)-1) or checkP(delete_j,0,len(delete_j)-1)
            i+=1
            j-=1
        return True
        