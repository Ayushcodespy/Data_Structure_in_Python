class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SLL:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head == None
    
    def insert_at_start(self, data):
        new = Node(data, self.head)
        self.head = new