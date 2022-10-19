class Solution:
    def minimumBuckets(self, street: str) -> int:
        count=0
        lst=list(street)
        for i in range(len(lst)):
            if lst[i]=="H":
                if i > 0 and lst[i-1]== "B":
                    continue
                if i+1<len(lst) and lst[i+1]==".":
                    lst[i+1]="B"
                    count+=1
                elif lst[i-1]=="." and i-1>=0:
                    lst[i-1]="B"
                    count+=1
                else:
                    return -1 
        return count