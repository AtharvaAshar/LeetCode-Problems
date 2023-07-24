class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def recurs(haystack,needle,index):
            if len(haystack)<len(needle):
                return -1
            
            if haystack ==needle:
                return index
            if haystack[:len(needle)]==needle:
                return index
            return recurs(haystack[1:],needle,index+1)
        return recurs(haystack,needle,0)
            