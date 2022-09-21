# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverse(self,head):
    #     previousnode=None
    #     currentnode=head
    #     # nextnode=head.next
    #     while(currentnode):
    #         nextnode=currentnode.next
    #         currentnode.next=previousnode
    #         previousnode=currentnode
    #         currentnode=nextnode
    #     reversednodehead=previousnode
    #     return reversednodehead
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if head.next==None:
        #     return None
        # reverse=self.reverse(head)
        # node=ListNode()
        # while n>0:
        #     node=reverse.next
        #     n-=1
        # node.val=node.next.val
        # node.next=node.next.next
        # return self.reverse(reverse)
        newnode = ListNode(0, head)
        st1 = newnode
        st2 = head
        for i in range(n):
            st2 = st2.next
        while st2:
            st2 = st2.next
            st1 = st1.next
        st1.next = st1.next.next
        return newnode.next
        
            