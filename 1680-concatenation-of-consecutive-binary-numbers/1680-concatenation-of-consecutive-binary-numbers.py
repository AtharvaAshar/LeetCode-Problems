class Solution:
    def concatenatedBinary(self, n: int) -> int:
        my_lst=[]
        my_lst_str=''
        for i in range(1,n+1):
            a=bin(i).replace("0b","")
            my_lst.append(a)
        my_lst_str = ''.join(map(str, my_lst))
        c=int(my_lst_str,2)
        return c%(10**9+7)
   
            
                
        