class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if (n==1):
            return 1
        one=self.findTheWinner(n-1 , k)
        two=(one+k)%n
        if(two==0):
            return n
        else:
            
            return two
    