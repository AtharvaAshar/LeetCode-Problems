# Function should return an integer value
def convertFive(n):
    # Code here
    def helper(n):
        if n==0: return 0
        digit=n%10
        if digit==0:
            digit=5
            
        return helper(n//10)*10 +digit
    
    if n==0:
        return 5
    else:
        return helper(n)

#{ 
 # Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
# } Driver Code Ends