class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l=0
        r=n-1
        area=0
        while(l<r):
        
            lh=height[l]
            rh=height[r]
              
            curr=(r-l)*min(lh,rh)
            area=max(area,curr);
    
            if(lh<rh):
                l+=1
            else:
                r-=1
        
    
    
        return area