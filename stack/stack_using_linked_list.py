class Node:
    def __init__(self,val,nxt):
        self.val = val
        self.nxt = nxt
class SLL:
    def __init__(self):
        head = None

    def insert_at_start(self,val):
        if head is None:
            head = Node(val,None)
        else:
           head =  Node(val,head)
                

        

