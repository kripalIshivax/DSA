class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    # Insert at end
    def insert(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    # Print list
    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.item, end=" -> ")
            temp = temp.next

        print("None")

    # Insert at beginning
    def insert_at_start(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

        if self.last is None:
            self.last = new_node

    def delete_from_start(self):
        self.head = self.head.next
        if self.head is None:
            raise IndexError("empty")        

    # Delete by value
    def delete(self, value):
        temp = self.head
        prev = None

        while temp is not None:
            if temp.item == value:
                if prev is None:
                    self.head = temp.next
                else:
                    prev.next = temp.next

                if temp == self.last:
                    self.last = prev

                return
            prev = temp
            temp = temp.next

        print("Value not found")

    # Search element
    def search(self, value):
        temp = self.head

        while temp is not None:
            if temp.item == value:
                return True
            temp = temp.next

        return False



s1 = SinglyLinkedList()

s1.insert(10)
s1.insert(13)
s1.insert(14)
s1.insert(44)
s1.insert(55)
s1.insert(23)

print("List:")
s1.print_list()

# print("Search 44:", s1.search(44))

# s1.delete(14)
# print("After deleting 14:")
# s1.print_list()

# s1.insert_at_start(5)
# print("After inserting at start:")
# s1.print_list()