class Solution:
   
    def countGoodSubstrings(self, s: str) -> int:
        def containsDuplicate(sub_str):
            dict={}
            for i in range(len(sub_str)):
                if sub_str[i] not in dict:
                    dict[sub_str[i]]=1
                else:
                    return True
            return False
        l=[]
        number=0
        for i in range(len(s)-2):
            a=''
            a=s[i:i+3]
            l.append(a)
        for i in l:
            if containsDuplicate(i)==False:
                number+=1
        return number
    
            
        