class Node:
    def __init__(self, data=None, prev=None, _next=None):
        self.prev = prev
        self.data = data
        self.next = _next


class DLL:

    def __int__(self, head=None):
        self.head = head

    def empty(self):
        return self.head is None

