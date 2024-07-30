class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next


class SLL:
    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None

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

    def insert_after(self, index, data):
        if self.is_empty():
            print("List is empty")
            return

        temp = self.head
        for i in range(index):
            if temp is None:
                print("Index is out of bounds.")
            temp = temp.next

        if temp is None:
            print("Index is out of bounds.")
            return

        new = Node(data, temp.next)
        temp.next = new

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="  ")
            temp = temp.next
        print("\n")


def runcode(arr):
    print('''\n Select operations in Linked List: 
        1. Insert at start
        2. Insert at last
        3. Insert at specific place
        4. Show list''')
    choice = int(input("Select Operation : "))
    if choice == 1:
        data = int(input("Enter data to insert : "))
        arr.insert_at_start(data)

    elif choice == 2:
        data = int(input("Enter data to insert : "))
        arr.insert_at_last(data)

    elif choice == 3:
        data = int(input("Enter data to insert : "))
        index = int(input("In which place you want to insert : "))
        index = index - 1
        arr.insert_after(index, data)

    elif choice == 4:
        arr.print_list()

    else:
        print("Please select a correct option")


lst = SLL()
loop = 1
while loop == 1:
    runcode(lst)
    loop = int(input("Press 1 to continue : "))
