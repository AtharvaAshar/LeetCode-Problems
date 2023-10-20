class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=defaultdict(list)
        for i in strs:
            count =[0]*26
            for j in range(len(i)):
                count[ord(i[j])-ord("a")]+=1
            d[tuple(count)].append(i)
        return d.values()
