class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp=x
        y=0
        if(x<0):
            return False
        else:
            while(x>0):
                d= x%10
                y= y*10 + d
                x=x//10
            if(temp==y):
                return True
            else:
                return False
        