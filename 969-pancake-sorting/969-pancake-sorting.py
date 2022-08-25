class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(index):
            arr[0:index]=reversed(arr[0:index])
        n=len(arr)
        result=[]
        for i in range(n):
            max_val=max(arr[0:n-i])
            max_idx=arr.index(max_val)+1
            flip(max_idx)
            result.append(max_idx)
            flip(n-i)
            result.append(n-i)
        return result
        