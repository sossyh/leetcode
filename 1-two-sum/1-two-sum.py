class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)):
            k=i+1
            for j in range(k,len(nums)):
                if(nums[i]+nums[j]==target):
                    result.append(i)
                    result.append(j)
        return result