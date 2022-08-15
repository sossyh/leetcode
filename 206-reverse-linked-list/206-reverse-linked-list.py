# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previousnode=None
        currentnode=head
        # nextnode=head.next
        while(currentnode):
            nextnode=currentnode.next
            currentnode.next=previousnode
            previousnode=currentnode
            currentnode=nextnode
        reversednodehead=previousnode
        return reversednodehead
        
        