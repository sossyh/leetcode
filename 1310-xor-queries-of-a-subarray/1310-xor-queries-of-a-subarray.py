class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result=[]
        lst=[arr[0]]
        for i in arr[1:]:
            lst.append(lst[-1]^i)
        
        for i in queries:
            if i[0]==0:
                result.append(lst[i[1]] )
            else:
                result.append(lst[i[1]]^lst[i[0]-1])
        return result