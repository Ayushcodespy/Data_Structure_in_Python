# program to perform bubble sorting in given list

def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range(len(arr)-x-1):
            if(arr[y] > arr[y+1]):
                temp = arr[y]
                arr[y] = arr[y+1]
                arr[y+1] = temp

lst = [11,13,42,14,76,39,45,31]
print(f"Unsorted List : \n {lst} \n")

bubble_sort(lst)
print(f"Sorted List : \n {lst}")

