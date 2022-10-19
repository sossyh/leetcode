class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n =  len(prices)
        descentp = [1]*n
        for i in range(1,n):
            if prices[i] +1 == prices[i-1]:
                descentp[i] += descentp[i-1]
        return sum(descentp)