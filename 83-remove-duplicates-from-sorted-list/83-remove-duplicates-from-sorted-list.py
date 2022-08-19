# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return head
        current=head
        # nex=current.next
        while(current and current.next):
            # nex=current.next
            if(current.val==current.next.val):
                current.next=current.next.next
            else:
                current=current.next
            # nex=nex.next
        return head