class Solution:
    def reverseWords(self, s: str) -> str:
        reverse_string=' '
        l=s.split()
        a=[]
        for i in l:
            i=i[::-1]
            a.append(i)
        reverse_string=reverse_string.join([str(ele)for ele in a])
        return reverse_string