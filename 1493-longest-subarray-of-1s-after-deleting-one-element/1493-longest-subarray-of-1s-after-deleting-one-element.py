class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result, leftp, k = 0, 0, 1
        for rightp in range(len(nums)):
            if nums[rightp] == 0:
                k -= 1
            if k < 0:
                if nums[leftp] == 0:
                    k += 1
                leftp += 1
            result = max(result, rightp-leftp)
        return result