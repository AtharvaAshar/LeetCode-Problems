class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n=len(req_skills)
        m=len(people)
        d={}
        for i in range(n):
            d[req_skills[i]]=i
        dp={0:[]}
        for i,p in enumerate(people):
            curr_skill_val=0
            for skill in p:
                curr_skill_val=curr_skill_val | 1<<d[skill]
            for prev,need in dict(dp).items():
                comb=prev | curr_skill_val
                if comb==prev: 
                    continue
                if comb not in dp or len(dp[comb])>len(need)+1:
                    dp[comb]=need + [i]
                
        return dp[(1 << n) - 1]