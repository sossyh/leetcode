# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        linkedlists = head
        while linkedlists:
            result.append(linkedlists.val)
            linkedlists = linkedlists.next
        
        result.sort()
        
        linkedlists = head
        for i in range(len(result)):
            linkedlists.val = result[i]
            
            linkedlists = linkedlists.next
        
        return head