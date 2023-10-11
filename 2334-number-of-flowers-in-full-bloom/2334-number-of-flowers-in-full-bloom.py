class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        def binarySearch(A,target):
            l,r=0,len(A)
            while l<r:
                mid=(l+r)//2
                if target <A[mid]:
                    r=mid
                else:
                    l=mid+1
            return l
        in_bound,out_bound=[],[]
        
        for i in flowers:
            in_bound.append(i[0])
            out_bound.append(i[1]+1)
        
        in_bound.sort()
        out_bound.sort()
        ans=[0]*len(people)
        for i in range(len(people)):
            e=binarySearch(out_bound,people[i])
            s=binarySearch(in_bound,people[i])
            ans[i]=s-e
        return ans
            
