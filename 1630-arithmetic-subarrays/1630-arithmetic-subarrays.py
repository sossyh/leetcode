class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result=[]
        flag=True
        for i in range(len(l)):
            newarr=nums[l[i]:r[i]+1]
            print(newarr)
            newarr.sort()
            d=newarr[1]-newarr[0]
            j=0
            while (j<len(newarr)):
                flag=True
                k=j+1
                if (k<len(newarr)):
                    if ((newarr[k]-newarr[j])!=d):
                        flag=False
                        break
                        print(newarr[k]-newarr[j])

                j=j+1
                
            if(flag==True):
                result.append(True)
            else:
                result.append(False)
        return result