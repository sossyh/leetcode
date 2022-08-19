from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.itemlist=SortedList()
        self.count=0

    def addNum(self, num: int) -> None:
        self.itemlist.add(num)
        # self.itemlist.sort()
        self.count+=1
        

    def findMedian(self) -> float:
        # length=len(self.itemlist)
        if(self.count%2!=0):
            # medianindex=int((length+1)/2)
            return self.itemlist[self.count//2]
        else:
            # first=self.itemlist[int((length/2)-1)]
            # second=self.itemlist[int(length/2)]
            median=((self.itemlist[int((self.count/2)-1)])+(self.itemlist[int(self.count/2)]))/2
            return median
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()