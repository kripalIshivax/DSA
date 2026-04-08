class Deck:
    def __init__(self):
        self.myList = []

    def insert_from_front(self,val):
        self.myList.insert(0,val)
    def insert_from_last(self,val):
        self.myList.append(val)
    def delete_from_front(self):
        self.myList.pop(0)
    def delete_from_last(self):
        self.myList.pop()
    def printDeck(self):
        for item in self.myList:
            print(item)
    def is_empty(self):
        if len(self.myList)>0:
            return False
        else:
            return True
    def size(self):
        return len(self.myList)
    def get_front(self):
        return self.myList[0]
    def get_rear(self):
        length = len(self.myList)-1
        return self.myList[length]

d = Deck()
d.insert_from_front(10)
d.insert_from_front(20)
d.insert_from_last(30)
d.insert_from_last(40)
d.printDeck()
d.delete_from_last()
d.delete_from_front()
print("------------------------")
d.printDeck()
print(d.is_empty())
print(d.size())
print(d.get_front())
print(d.get_rear())






