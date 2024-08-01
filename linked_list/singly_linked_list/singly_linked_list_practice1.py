class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        return self.head is None

    def insert_at_start(self, data):
        new = Node(data, self.head)
        self.head = new

    def insert_at_last(self, data):
        new = Node(data)
        if not self.empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new
        else:
            self.insert_at_start(data)

    def print_lst(self):
        if not self.empty():
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("List is empty")


lst = SinglyLinkedList()
lst.insert_at_start(12)
lst.insert_at_last(24)
lst.insert_at_start(71)
lst.print_lst()
