class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque()
        length = len(nums)
        answer = length + 1
        
        pre = [0] + list(accumulate(nums))

        for i in range(length + 1):
            while q and pre[i] - pre[q[0]] >= k:
                answer = min(answer, i - q.popleft())
            while q and pre[i] <= pre[q[-1]]:
                q.pop()
            q.append(i)
        if answer <= length:
            return answer  
        else:
            return -1