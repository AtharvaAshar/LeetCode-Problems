class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c,out={},[]
        for n in nums:
            c[n] = c.get(n, 0) + 1
        
        c=[(-v,k) for k,v in c.items()]
        heapq.heapify(c)
        for i in range(k):
            item=heapq.heappop(c)
            out.append(item[1])
        return out
        
