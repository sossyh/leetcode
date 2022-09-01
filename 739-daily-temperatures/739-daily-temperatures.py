class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
     
        tempstack=[]
        indexstack=[]
        for idx, temp in enumerate(temperatures):
            while tempstack and tempstack[-1]<temp:
                topidx=indexstack.pop()
                result[topidx]=idx - topidx
                tempstack.pop()
            tempstack.append(temp)
            indexstack.append(idx)
            
        return result