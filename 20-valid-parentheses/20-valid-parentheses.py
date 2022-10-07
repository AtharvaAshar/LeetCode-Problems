class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={')':'(','}':'{',']':'['}
        for i in s:
            if i in dict.values():
                stack.append(i)
            elif stack and stack[-1]==dict[i]:
                stack.pop()
            else:
                return False
        return stack==[]