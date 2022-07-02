class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        newlist=[]
        for item in nums:
            newlist.append(int(item))
        newlist.sort(reverse=True)
        kth=newlist[k-1]
        return str(kth)