# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def list_node_to_list(list_node):
            array = []
            while list_node:
                array.append(list_node.val)
                list_node = list_node.next
            return array

        def list_to_list_node(arr):
            curr = list_node = ListNode()
            for num in arr:
                curr.next = ListNode(num)
                curr = curr.next
            return list_node.next

        result = []
        for list_node in lists:
            result += list_node_to_list(list_node)
        return list_to_list_node(sorted(result))