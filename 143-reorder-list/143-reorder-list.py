# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverse(self,head):
        previousnode=None
        currentnode=head
        # nextnode=head.next
        while(currentnode):
            nextnode=currentnode.next
            currentnode.next=previousnode
            previousnode=currentnode
            currentnode=nextnode
        # reversednodehead=previousnode
        return previousnode
    def merge(self,l1,l2):
        
        while l1 and l2:
           
            temp=l1.next
            l1.next=l2
            l1=l2
            l2=temp

    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return
        l1=head
        secondHalfHead=head
        secondHalfTail=head
        firstHalfTail=None
        while secondHalfTail and secondHalfTail.next:
            firstHalfTail=secondHalfHead
            secondHalfHead=secondHalfHead.next
            secondHalfTail=secondHalfTail.next.next
        firstHalfTail.next=None
        l2=self.reverse(secondHalfHead)
        # print(l1)
        # print(l2)
        self.merge(l1,l2)
            
        