class Node:
    def __init__(self,left,item,right):
        self.left = left
        self.item = item
        self.right = right
class Tree:
    def __init__(self):
        self.root = None
    def trev(self,temp):
        if temp is None:
            return
        print("item",temp.item)
        if temp.left is None and temp.right is None:
            return
        if temp.left is None:
            self.trev(temp.right)
        elif temp.right is None:
            self.trev(temp.left)
        else:
            self.trev(temp.left)
            self.trev(temp.right)
    
    def callTrev(self):
        self.trev(self.root)
        
        
    def insert(self,item):
        newNode = Node(None,item,None)
        if self.root is None:
            self.root1 = newNode
        else:
            temp = self.root
            while temp.left is not None and temp.right is not None:
                print("item",temp.item)
                

t = Tree()
t.callTrev()
                
