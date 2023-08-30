#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
    # code here
    # Brute Force
    # ans=[]
    # for i in range(N-K+1):
    #     min_num=10**9
    #     for j in range(K):
    #         if A[i+j]<0:
    #             min_num=A[i+j]
    #             break
    #     if min_num==10**9 : ans.append(0)
    #     else:
    #         ans.append(min_num)
    
    # return ans
    q=deque([])
    ans=[]
    i=0
    j=0
    while j<N:
        if A[j]<0:
            q.append(A[j])
        
        if j-i+1<K:
            j+=1
        
        elif j-i+1==K:
            if len(q)==0:
                ans.append(0)
            else:
                ans.append(q[0])
                if A[i]==q[0]:
                    q.popleft()
            j+=1
            i+=1
    return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends