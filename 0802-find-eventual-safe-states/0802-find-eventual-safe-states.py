class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res=[]
        n=len(graph)
        visited=[-1]*len(graph) #-1 for not visited
        def isCycle(i):
            visited[i]=0
            for v in graph[i]:
                if visited[v]==0 or (visited[v]==-1 and isCycle(v)):
                    return True
            visited[i]=1
            res.append(i)
            return False
        for i in range(n):
            if visited[i]==-1: isCycle(i)
        return sorted(res)
            
            