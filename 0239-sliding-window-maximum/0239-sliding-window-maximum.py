class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        n=len(nums)
        q=deque([0])
        for i in range(n):
            while q and q[0]<=i-k:
                q.popleft()
            while q and nums[q[-1]]<=nums[i]:
                q.pop()
            q.append(i)
            l.append(nums[q[0]])
        return l[k-1:]