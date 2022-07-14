class Solution:
    def compare(self,num1,num2):
        if(int(str(num1)+str(num2))>int(str(num2)+str(num1))):
            return str(num1)+str(num2)
        else:
            return str(num2)+str(num1)
        
    def largestNumber(self, nums: List[int]) -> str:
        result=""
        b=0
        a=sorted(nums,key=str)
        a.reverse()
        for i in range(len(a)):
             a[i]=str(a[i])
        for j in range(len(a)):
            for k in range(j+1,len(a)):
                if(a[j][0]==a[k][0]):
                    b=self.compare(int(a[j]),int(a[k]))
                    result=result+b
            if(b==0):
                result=result+a[j]
            
        
        return result
