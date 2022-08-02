class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        result=0
        nums.sort()
        n=(len(nums)/2)+1
        m=int(n)
        for i in range(m):
            l=nums[i]+nums[-1-i]
            if(l>result):
                result=l
        return result
        