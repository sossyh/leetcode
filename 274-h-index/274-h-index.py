class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        result=1
        while result<=n:
            if(citations[n-result]<result):
                break
            result=result+1
        
            
        return result-1
    
    
    