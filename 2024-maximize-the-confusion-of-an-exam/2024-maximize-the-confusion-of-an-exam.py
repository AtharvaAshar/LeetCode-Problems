class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        best=0
        n=len(answerKey)
        for correct in ["T","F"]:
            #count number of opposite value between left and right
            count=0
            start=0
            for i in range(n):
                if answerKey[i]!=correct:
                    count+=1
                while count>k:
                    if answerKey[start]!=correct:
                        count-=1
                    start+=1  
                best=max(best,i-start+1)
        return best