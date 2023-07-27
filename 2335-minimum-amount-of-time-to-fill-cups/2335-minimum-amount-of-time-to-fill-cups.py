class Solution:
    def fillCups(self, amount: List[int]) -> int:
        #    Always trying to fill cups with largest values
            amount=sorted(amount,reverse=True)
            count=0
            while amount[0]>0:
                amount[0]-=1
                amount[1]-=1
                count+=1
                amount=sorted(amount,reverse=True)
        
            return count
         