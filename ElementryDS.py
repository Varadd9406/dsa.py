class Stacks:
    def __init__(self):
        self.arr = []
        self.top = 0

    def insert(self, x):
        self.arr.append(x)
        self.top += 1

    def remove(self):
        if self.top != 0:
            self.top -= 1
            del self.arr[self.top]
        else:
            raise Exception("No Element to delete")


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def listSearch(self, key):
        x = self.head
        while x is not None and x.data != key:
            x = x.next
        return x

    def listInsert(self,x):
        x.next = self.head
        if self.head is not None:
            self.head.prev = x


l = LinkedList()

l.head = Node(1)
second = Node(56)
third = Node(3)
l.head.next = second
second.next = third

l.printList()