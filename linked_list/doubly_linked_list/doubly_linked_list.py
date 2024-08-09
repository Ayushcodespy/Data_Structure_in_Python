class Node:
    def __init__(self, data=None, prev=None, _next=None):
        self.prev = prev
        self.data = data
        self.next = _next


class Dll:
    def __init__(self, head=None):
        self.head = head

    def insert_at_start(self, data):
        new = Node(data, None, self.head)
        self.head = new

    def insert_at_last(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def show(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next


dll = Dll()

dll.insert_at_start(10)
dll.insert_at_start(20)
dll.insert_at_start(30)
dll.insert_at_last(40)
dll.insert_at_start(5)

dll.show()
