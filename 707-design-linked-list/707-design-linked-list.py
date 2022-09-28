class Node:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode
class MyLinkedList:

    def __init__(self):
        self.head=Node()
        self.capacity=0

    def get(self, index: int) -> int:
        if index >= self.capacity:
            return -1

        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        previous = self.head
        newNode = Node(val, previous.next)
        previous.next = newNode
        self.capacity += 1

    def addAtTail(self, val: int) -> None:
        previous = self.head
        for i in range(self.capacity):
            previous = previous.next
        newNode = Node(val, previous.next)
        previous.next = newNode
        self.capacity += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.capacity: 
            return

        previous = self.head
        for i in range(index):
            previous = previous.next
        newNode = Node(val, previous.next)
        previous.next = newNode
        self.capacity += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.capacity:  
            return

        previous = self.head
        for i in range(index):
            previous = previous.next

        previous.next = previous.next.next
        self.capacity -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)