# function to sort the list
def buble_sort(arr):
    loop = len(arr)
    for i in range(loop):
        for j in range (loop-1-i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


# Taking input the elements of the list from user
n = int(input(f"How many elements you want to enter : "))
lst = []
for x in range(n):
    element = int(input(f"Enter element {x+1} : "))
    lst.append(element)

# Printing the list
print(f"Unsorted List: {lst}")
buble_sort(lst)     # Function Call
print(f"Sorted lost : {lst}")
