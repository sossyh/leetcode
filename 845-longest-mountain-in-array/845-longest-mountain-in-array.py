class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n, max_len = len(arr), 0
        state, length = 0, 1
        for i in range(n-1):
            if state in [0, 1] and arr[i+1] > arr[i]:
                state, length = 1, length + 1
            elif state == 2 and arr[i+1] > arr[i]:
                state, length = 1, 2
            elif state in [1, 2] and arr[i+1] < arr[i]:
                state, length = 2, length + 1
                max_len = max(length, max_len)
            else:
                state, length = 0, 1
                
        return max_len