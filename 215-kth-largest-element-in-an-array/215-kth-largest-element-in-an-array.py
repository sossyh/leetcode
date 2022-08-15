class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=sorted(nums)
        
        return heap[-k]
#         while(nums and heap[-1]>nums[0]):
#             nums.pop(0)
            