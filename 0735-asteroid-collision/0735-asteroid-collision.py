class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]
        for i in asteroids:
            while len(stack)>0 and i<0 and stack[-1]>0:
                if stack[-1]==-i:
                    stack.pop()
                    break
                elif stack[-1]<-i:
                    stack.pop()
                    continue
                elif stack[-1]>-i:
                    break
            else:
                stack.append(i)
        
        return stack
            