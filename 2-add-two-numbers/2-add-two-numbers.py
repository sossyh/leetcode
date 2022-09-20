# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # newhead=ListNode()
        # l3=newhead
        # carry=0
        # while l1 or l2:
        #     l1val=l1.val if l1!=None else 0
        #     l2val=l2.val if l2!=None else 0
        #     newsum = l1val+l2val+carry
        #     carry=newsum/10
        #     lastdigit=newsum%10
        #     newnode=ListNode(lastdigit)
        #     l3.next=newnode
        #     if(l1!=None):
        #         l1=l1.next
        #     if(l2!=None):
        #         l2=l2.next
        #     l3=l3.next
        # if carry>0:
        #     newnode=ListNode(carry)
        #     l3.next=newnode
        #     l3=l3.next
        # return newhead.next
        
        num1 = ''
        while l1 :
            num1 = str(l1.val)  + num1  
            l1 = l1.next
        num2 = ''
        while l2 :
            num2 = str(l2.val)  + num2  
            l2 = l2.next
        numssum = str(int(num1) + int(num2))
        reversenode = ListNode(val = numssum[-1])
        numssum = numssum[:-1]
        temp = reversenode
        while numssum:
            newnode = ListNode(val = numssum[-1])
            temp.next = newnode
            temp = temp.next 
            numssum = numssum[:-1]
            
        return reversenode
                