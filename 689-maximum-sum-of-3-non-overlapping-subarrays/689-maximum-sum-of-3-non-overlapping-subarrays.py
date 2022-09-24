class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        f = defaultdict(int)
        s = defaultdict(int)
        g = defaultdict(tuple)
        for i in range(len(nums)):
            s[i] = s[i-1] + nums[i]
            for j in range(3):
                g[i, j] = g[i-1, j]
                f[i, j] = f[i-1, j]
                if s[i] - s[i-k] + f[i-k, j-1] > f[i, j]:
                    f[i, j] = s[i] - s[i-k] + f[i-k, j-1]
                    g[i, j] = g[i-k, j-1] + (i - k + 1,)
        return g[len(nums)-1, 2]