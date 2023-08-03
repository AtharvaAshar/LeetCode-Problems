class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
        }
        def helper(comb,index,digits):
            if len(digits)==index:
                ans.append(comb)
                return
            letters=d[int(digits[index])]
            for c in letters:
                helper(comb+c,index+1,digits)
        if digits=="":
            return []
        ans=[]
        helper("",0,digits)
        return ans