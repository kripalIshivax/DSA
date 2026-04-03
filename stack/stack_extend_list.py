class Stack(list):
    def __init__(self):
        # self.myList=[]
        pass

    def push(self, item):
        super().append(item)

    def pop(self):
        super().pop()

    def peek(self):
        length = len(self)
        if length == 0:
            raise Exception("Empty List!")
        else:
            return self[length - 1]

    def size(self):
        return len(self)

    def is_empty(self):
        if len(self) > 0:
            False
        else:
            True


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.is_empty()
stack.size()
