class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result=[]
        for i in matrix:
            for j in i:
                result.append(j)
        result.sort()
        return result[k-1]