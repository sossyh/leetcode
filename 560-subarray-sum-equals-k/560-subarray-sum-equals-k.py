class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         subarray=[]
#         count=0
#         for i in range(len(nums)+1):
#             for j in range(i):
#                 subarray.append(nums[j:i])
#         for i in subarray:
#             if(sum(i)==k):
#                 count+=1
                
#         return count
        dict_ = defaultdict(int)
        sum_ = 0
        count=0
        dict_[0] = 1
        for i in nums:
            sum_ += i
            count += dict_.get(sum_ - k, 0)
            dict_[sum_]+=1
        return count
        