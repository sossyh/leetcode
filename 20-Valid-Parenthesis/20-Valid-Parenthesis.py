class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        d={"(":")","{": "}","[":"]"}
        for i in range(len(s)):
            if s[i] in d:
                stack.append(s[i])
            
            else:
                if(len(stack)==0):
                    return False
                elif(d[stack[-1]]==s[i]):
                    stack.pop(-1)
                else:
                    return False
            if(len(stack)==0):
                return True
