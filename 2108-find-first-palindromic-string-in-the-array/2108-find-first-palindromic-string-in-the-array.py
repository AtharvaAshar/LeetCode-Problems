class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def checkP(s,si,ei):
            if si==ei or ei<0:
                return True
            if s[si]!=s[ei]:
                return False
            return checkP(s,si+1,ei-1)
        for word in words:
            print(word)
            if checkP(word,0,len(word)-1):
                return word
        return ""