class Node:
    def __init__(self, data=None, _next=None):
        self.data = data
        self.next = _next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def empty(self):
        return self.head is None

    # -------- Insertion Operations ---------
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

    # -------- Delete Operations ---------
    def delete_first(self, a="first"):
        if self.empty():
            print("------- List doesnt have any node -------")

        else:
            temp = self.head
            self.head = temp.next
            print(f"------ {a} Node which contains {temp.data} is deleted ------")

    def delete_last(self):
        temp = self.head

        if self.empty():
            print("------- List doesnt have any node -------")

        elif temp.next is None:
            a = "last"
            self.delete_first(a)

        else:
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            prev.next = None
            print(f"------ Last Node which contains {temp.data} is deleted ------")

    # ------- Printing Linked List ---------
    def print_lst(self):
        if not self.empty():
            temp = self.head
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()
        else:
            print("List is empty")


def runcode(arr):
    choice = int(input("Select Operation : "))

    if choice == 0:
        print('''\n Select operations in Linked List: 
            0. Show Operations
            1. Insert at start
            2. Insert at last
            3. Insert at specific place
            4. Show list
            5. Delete First Node
            6. Delete Last Node''')

    elif choice == 1:
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

    elif choice == 6:
        arr.delete_last()

    else:
        print("Please select a correct option")


lst = SinglyLinkedList()
print('''\n Select operations in Linked List: 
            0. Show Operations
            1. Insert at start
            2. Insert at last
            3. Insert at specific place
            4. Show list
            5. Delete First Node
            6. Delete Last Node''')
loop = 1
while loop == 1:
    runcode(lst)
    loop = int(input("Press 1 to continue : "))
