class Node:
    def __init__(self,left,item,right):
        self.left = left
        self.item = item
        self.right = right
class BST:
    def __init__(self):
        self.root = None

    def insert(self,item,temp):
        if temp is None:
            self.root = Node(None,item,None)
            return
        if temp.item > item:
            if temp.left is None:
                temp.left = Node(None,item,None)
                return
            else:
                self.insert(item,temp.left)
        else:
            if temp.right is None:
                temp.right = Node(None,item,None)
                return
            else:
                self.insert(item,temp.right)
                        
    def call_insert(self,item):
        self.insert(item,self.root)

    def printBst(self,temp):
        if temp is None:
            return
        print("item",temp.item)
        if temp.left is None and temp.right is None:
            return
        if temp.left is None:
            print("right")
            self.printBst(temp.right)
        elif temp.right is None:
            print("left")
            self.printBst(temp.left)
        else:
           print("both")
           self.printBst(temp.left)
           self.printBst(temp.right)

    def call_printBst(self):
        self.printBst(self.root)
    def in_order_trev(self,temp):
        if temp is None:
            return
        if temp.left is None and temp.right is None:
            return
        if temp.right is None:
            self.in_order_trev
bst = BST()
bst.call_insert(100)
bst.call_insert(99)
bst.call_insert(98)
bst.call_insert(102)
bst.call_insert(332)
bst.call_insert(3)
bst.call_insert(4)
bst.call_printBst()


