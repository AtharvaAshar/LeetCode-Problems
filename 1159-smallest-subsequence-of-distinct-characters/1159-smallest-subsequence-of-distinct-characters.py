class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack=[]
        in_stack=set()
        rightmostIdx={char:idx for idx,char in enumerate(s)}
        for idx,char in enumerate(s):
            if char not in in_stack:
                while stack and char<stack[-1] and idx<rightmostIdx[stack[-1]]:
                    in_stack.remove(stack.pop())
                stack.append(char)
                in_stack.add(char)

        return "".join(stack)