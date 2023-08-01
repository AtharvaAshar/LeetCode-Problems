class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def helper(start,n,k,sub,ans):
            if k==0:
                ans.append(sub[:])
                return
            for i in range(start,n-k+2):
                sub.append(i)
                helper(i+1,n,k-1,sub,ans)
                sub.pop()
        ans=[]
        helper(1,n,k,[],ans)
        return ans
                
            