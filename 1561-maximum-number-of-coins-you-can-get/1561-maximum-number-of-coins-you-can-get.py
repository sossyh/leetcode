class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        me=0
        n=int(len(piles)/3)
        piles.sort()
        pile=piles[n:]
        pile.reverse()
        i=1
        while(i<len(pile)):
            me=me+pile[i]
            i=i+2
            
            
              
        # for i in range(len(pile)):
        #     if((i+1)>=len(pile)):
        #        break
        #     me=me+pile[i+1]
            
        return me