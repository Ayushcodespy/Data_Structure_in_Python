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

    def insert_at_last(self, data):
        new = Node(data)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new

        else:
            self.head = new

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="  ")
            temp = temp.next

lst = SLL()
lst.insert_at_start(24)
lst.insert_at_start(27)
lst.insert_at_last(73)
lst.print_list()