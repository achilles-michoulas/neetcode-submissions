class MyLinkedList:

    def __init__(self):
        self.dummyHead = Node()
        self.dummyTail = Node()
        self.size = 0

        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def get(self, index: int) -> int:
        iterator = self.dummyHead.next
        
        if index < 0 or index >= self.size:
            return -1

        for _ in range(index):
            iterator = iterator.next
        
        return iterator.val
    
    def addAtHead(self, val: int) -> None:
        newHead = Node(val=val)
        prevHead = self.dummyHead.next

        prevHead.prev = newHead
        newHead.next = prevHead
        
        self.dummyHead.next = newHead
        newHead.prev = self.dummyHead

        self.size += 1

    def addAtTail(self, val: int) -> None:
        newTail = Node(val=val)
        prevTail = self.dummyTail.prev

        prevTail.next = newTail
        newTail.prev = prevTail

        self.dummyTail.prev = newTail
        newTail.next = self.dummyTail

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        iterator = self.dummyHead
        count = 0
        
        if index == self.size:
            self.addAtTail(val)
            return
        
        if index < 0 or index > self.size:
            return

        while count < index:
            iterator = iterator.next
            count += 1
        
        newNode = Node(val=val)

        before = iterator
        after = iterator.next
        
        newNode.prev = before
        newNode.next = after

        before.next = newNode
        after.prev = newNode

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        iterator = self.dummyHead
        count = 0

        if index < 0 or index >= self.size:
            return
       
        while count < index:
            iterator = iterator.next
            count += 1
        
        before = iterator
        after = iterator.next.next

        before.next = after
        after.prev = before

        self.size -= 1
        

class Node:

    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)