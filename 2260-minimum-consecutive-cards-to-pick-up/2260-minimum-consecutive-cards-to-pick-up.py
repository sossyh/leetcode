class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d={}
        min_=sys.maxsize
        for idx,i in enumerate(cards): 
            if i in d:
                a=idx-d[i]
                min_=min(min_,a)
                d[i]=idx
            else:
                d[i]=idx
        if(min_!=sys.maxsize):
            return min_+1
        return -1