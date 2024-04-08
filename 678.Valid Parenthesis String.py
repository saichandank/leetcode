class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        star=[]
        for i in range(len(s)):
            if s[i]==')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif s[i]=='(':
                stack.append(i)
            else:
                star.append(i)
        
        while stack and star:
            if stack.pop() > star.pop():
                return False 

        return not stack
        

        
