# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values=[]
        while head:
            values.append(head.val)
            head=head.next
        max_=0
        for i in range(len(values)):
            sum_=values[i]+values[-1-i]
            if(sum_>max_):
                max_=sum_
        return max_