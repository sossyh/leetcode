class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result=[]
        for i in points:
            e=(i[0])**2 + (i[1])**2
            s=math.sqrt(e)
            point=[s,i[0],i[1]]
            result.append(point)
           
        result.sort()
        for i in result:
            del(i[0])
        
        return result[:k]