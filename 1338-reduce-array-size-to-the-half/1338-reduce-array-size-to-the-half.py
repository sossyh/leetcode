class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d={}
        frequency=[]
        n=len(arr)
        for i in arr:
             d[i] = (d[i] + 1) if (i in d) else 1
            
            # count=0
            # for j in arr:
            #     if(i==j):
            #         count=count+1
            #         d[i]=count
        for i in d:
            frequency.append(d[i])
        
        frequency.sort(reverse=True)
        sum_=0
        c=0
        for k in frequency:
            c=c+1
            sum_=sum_+k
            if(sum_>=n/2):
                return c
                
            
        return  frequency     