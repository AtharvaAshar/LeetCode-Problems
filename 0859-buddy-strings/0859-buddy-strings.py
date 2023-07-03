class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        diff=[]
        a=set()
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
            a.add(s[i])
        if len(diff)>2 or len(diff)==1: return False

        if len(diff)==2:
            return s[diff[0]]==goal[diff[1]] and goal[diff[0]]==s[diff[1]]
        return len(a)<len(s)