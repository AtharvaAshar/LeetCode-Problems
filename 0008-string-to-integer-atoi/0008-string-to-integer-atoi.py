class Solution:
    def myAtoi(self, s: str) -> int:
        numbers={str(i):i for i in range(10)}
        sign,empty,num=1,True,0
        for c in s:
            if empty:
                if c==" ":
                    continue
                elif c=="-":
                    sign=-1
                elif c.isdigit():
                    num=numbers[c]
                elif c!="+":
                    return 0
                empty=False
            else:
                if c.isdigit():
                    num=num*10+numbers[c]
                    if sign*num>(2**31)-1:
                        return (2**31)-1
                    elif sign*num<-2**31:
                        return -2**31
                else:
                    break
        return sign*num
                
            