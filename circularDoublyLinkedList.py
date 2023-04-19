class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None