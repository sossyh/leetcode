# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:
            k_temp = k
            kth_element = self.getNextKthElement(prevGroup, k)
            if not kth_element:
                break
            prev, curr = kth_element.next, prevGroup.next                
            while curr and k_temp > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                k_temp -= 1
            tmp = prevGroup.next
            prevGroup.next = kth_element
            prevGroup = tmp
        return dummy.next
            
    def getNextKthElement(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr