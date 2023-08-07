class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        n=len(s)
        _set=set()
        ans=0
        for right in range(n):
            if s[right] not in _set:
                _set.add(s[right])
                ans=max(ans,right-left+1)
            else:
                while s[right] in _set:
                    _set.remove(s[left])
                    left+=1
                _set.add(s[right])
        return ans