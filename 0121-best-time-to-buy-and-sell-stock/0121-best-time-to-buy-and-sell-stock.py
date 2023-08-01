class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        stack=[]
        for i in prices:
            if len(stack)==0:
                stack.append(i)
            elif i>stack[-1]:
                maxProfit=max(maxProfit,i-stack[-1])
            elif stack[-1]>i:
                stack.pop()
                stack.append(i)
        return maxProfit