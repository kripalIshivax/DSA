class Node:
    def __init__(self,prev,val,next):
        self.prev = prev
        self.val = val
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert(self,val):
        if self.head is None:
            self.head = Node(None,val,None)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            else:
                newNode = Node(temp,val,None)
                temp.next = newNode
    def printList(self):
         temp = self.head
         while temp.next is not None:
             print(temp.val)
             temp = temp.next
         else:
             print(temp.val)

    def insert_at_start(self,val):
        newNode = Node(None,val,self.head)

d = DoublyLinkedList()
d.insert(10)
d.insert(20)
d.insert(30)
d.insert(40)
d.printList()
