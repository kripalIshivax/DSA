class Node:
    def __init__(self,left = None,item = None, right = None):
        self.left = left 
        self.item = item
        self.right = right 
class BST:
    def __init__(self, root = None):
        self.root = root
    def insert(self,item):
        self.re_insert(item,self.root)
    def re_insert(self,item,root):
        if root is None:
            self.root = Node(None,item,None)
            return Node(None,item,None)
        elif item < root.item:
            root.left =  self.re_insert(item,root.left)
        elif item > root.item:
            root.right = self.re_insert(item,root.right)
        return
    def search(self,item):
        self.re_search(self.root,item)
    def re_search(self, root , item):
        if root is None or root.item == item:
            return root
        if data < root.item:
            return self.re_search(root.left,item)
        else:
            return self.re_search(root.right,item)
    def in_order_trev(self):
        self.io_trev(self,self.root):
    def io_trev(self,root):
        if root is None:
            return


