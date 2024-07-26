# function to perform insertion sort it takes a list as an argument
def insertion_sort(arr):
    l = len(arr)
    for i in range(1, l):
        current = arr[i]

        j = i-1
        while(j >= 0 and current < arr[j]):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = current
    return arr

# Main Program 
n = int(input("Enter length of the list : "))
lst = []
for x in range(n):
    value = int(input(f"Enter element {x+1} : "))
    lst.insert(x, value)

print(f"Unsorted List is {lst}")
lst = insertion_sort(lst)
print(f"Sorted List is {lst}")