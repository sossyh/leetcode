class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if(n>=1):
        #     if(n==1):
        #         return x
        #     else:
        #         return x*self.myPow(x,n-1)
        # else:
        #     if(n==0):
        #         return 1
        #     else:
        #         return (1/x)*self.myPow(x,n+1)
        return math.pow(x,n)