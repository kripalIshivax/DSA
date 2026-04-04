class Node:
    def __init__(self,val,next):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        head = None

    def is_empyt(self):
        if head is None:
            return True
        else:
            return False

    def push(self,val):
        newNode=Node(val,self.head)
        self.head = newNode

    def pop(self):
        data=self.head
        if 

