# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newnode=ListNode(0,head)
        previous=newnode
        current=head
        while current and current.next:
            if current.val==current.next.val:
                while current.next and current.val==current.next.val:
                    current=current.next
                previous.next=current.next
                current=current.next
                
            else: 
                previous=current
                current=current.next
        return newnode.next

            
        