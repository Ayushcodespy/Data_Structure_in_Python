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

    def inert_at_nth_place(self, data, index):
        if index == 0:
            self.insert_at_start(data)

        elif not self.empty():
            temp = self.head
            for i in range(index - 1):
                if temp is None:
                    print("Index is out of Bounds")
                    return
                temp = temp.next
            new = Node(data, temp.next)
            temp.next = new
        else:
            print("List is empty")
            return

    def print_lst(self):
        if not self.empty():
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("List is empty")

    def delete_first(self):
        temp = self.head
        self.head = temp.next


def runcode(arr):
    print('''\n Select operations in Linked List: 
        1. Insert at start
        2. Insert at last
        3. Insert at specific place
        4. Show list
        5. Delete first element''')
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
        arr.inert_at_nth_place(data, index)

    elif choice == 4:
        arr.print_lst()

    elif choice == 5:
        arr.delete_first()

    else:
        print("Please select a correct option")


lst = SinglyLinkedList()
loop = 1
while loop == 1:
    runcode(lst)
    loop = int(input("Press 1 to continue : "))
