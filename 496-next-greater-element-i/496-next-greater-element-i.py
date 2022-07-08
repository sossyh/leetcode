class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for i in nums1:
            for j in range(len(nums2)):
                if(i==nums2[j]):
                    a=len(result)
                    for k in range(j,len(nums2)):
                        if(nums2[k]>nums2[j]):
                            result.append(nums2[k])
                            break
                    if(a==len(result)):
                        result.append(-1)
        return result
        