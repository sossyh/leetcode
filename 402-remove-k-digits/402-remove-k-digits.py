class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result=""
        monotonicstack=[]
        for n in num:
            
            while(k>0 and monotonicstack and int(monotonicstack[-1])>int(n)):
                    # if():
                        monotonicstack.pop()
                        k=k-1
            monotonicstack.append(n)
        monotonicstack=monotonicstack[:len(monotonicstack)-k]
        
        for i in monotonicstack:
            result=result+str(i)
        
        if(result):
            result=int(result)
            return str(result)
        else:
            return "0"
        