class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count=[0]*26
        count1=[0]*26
        for i in s:
            count[ord(i)-ord("a")]+=1
        for j in t:
            count1[ord(j)-ord("a")]+=1
        if(count1==count):
            return True
        else:
            return False
        