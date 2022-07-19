class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count=0
        result=[]
        nums.sort()
        for i in nums:
            for j in range(k):
                if j+i+1 in nums:
                    count=count+1
            result.append(count)
            result.sort()
        return result[-1]
